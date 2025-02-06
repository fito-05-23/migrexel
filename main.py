import sys
import os
from PySide6.QtCore import Qt, QSortFilterProxyModel, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox, QFileDialog, QInputDialog, QAbstractItemView
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from widgets.ui_main_window import Ui_MainWindow  # Asegúrate de que la ruta sea correcta
from logic.message_handler import MessageHandler
from logic.context_menu_manager import ContextMenuManager  # Asegúrate de que la ruta sea correcta
from logic.database import create_connection, execute_sql  # Asegúrate de que la ruta sea correcta
from logic.excel_reader import read_excel
from logic.sql_generator import generate_create_table_sql, sanitizar_identificador, generate_insert_sql

# Configuración de DPI para monitores de alta resolución
os.environ["QT_FONT_DPI"] = "96"  # Solución para monitores de alta resolución

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Configuración de DPI para monitores de alta resolución
        os.environ["QT_FONT_DPI"] = "96"  # Solución para monitores de alta resolución

        # Cargar estilos desde el archivo QSS
        self.load_styles()

        # Inicializar la base de datos
        self.initialize_database()

        # Cargar la lista de archivos al iniciar la aplicación
        self.load_list_files()
        
        self.upload_sql()
        
        # Crear una instancia de ContextMenuManager
        self.context_menu_manager = ContextMenuManager(self)
        
        # Conectar el evento de clic derecho en listWidget_file_xls
        self.ui.listWidget_file_xls.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listWidget_file_xls.customContextMenuRequested.connect(self.show_context_menu_file_xls)

        # Conectar el evento de clic derecho en listWidget_sql
        self.ui.listWidget_sql.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listWidget_sql.customContextMenuRequested.connect(self.show_context_menu_sql)
        
        # Conectar botones a funciones
        self.ui.btn_convert_sql.clicked.connect(self.convert_sql)
        self.ui.btn_upload.clicked.connect(self.load_file)
        self.ui.btn_load_sql.clicked.connect(self.load_table_sql)
        self.ui.btn_search.clicked.connect(self.search_row)
        self.ui.btn_edit.clicked.connect(self.edit_data)
        self.ui.btn_sidebar.clicked.connect(self.toggle_content_light)
        
        # Configurar la selección de fila única
        self.ui.tableView_data.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView_data.setSelectionMode(QAbstractItemView.SingleSelection)

        # Configurar el modelo para permitir la edición
        self.model = QStandardItemModel()
        self.ui.tableView_data.setModel(self.model)
        #self.model.itemChanged.connect(self.on_item_changed)

        # Conectar la señal de tecla presionada
        self.ui.tableView_data.keyPressEvent = self.keyPressEventOverride

    def toggle_content_light(self):
        if self.ui.content_light.isVisible():
            self.ui.content_light.hide()
            self.sidebar_open = False
            self.ui.btn_sidebar.setIcon(QIcon(u":/icon/assets/icons/white/side_navigation_right_white.svg"))
            self.ui.btn_sidebar.setIconSize(QSize(24, 24))  # Ajusta el tamaño del icono según sea necesario
            self.ui.btn_sidebar.setText("")  # Ocultar el texto del botón si es necesario
        else:
            self.ui.content_light.show()
            self.sidebar_open = True
            self.ui.btn_sidebar.setIcon(QIcon(u":/icon/assets/icons/white/side_navigation_left_white.svg"))
            self.ui.btn_sidebar.setIconSize(QSize(24, 24))  # Ajusta el tamaño del icono según sea necesario
            self.ui.btn_sidebar.setText("")  # Ocultar el texto del botón si es necesario
            
    def initialize_database(self):
        # Ruta a la carpeta de la base de datos
        db_folder = os.path.join(os.getcwd(), "database")
        os.makedirs(db_folder, exist_ok=True)  # Crear la carpeta si no existe

        # Ruta a la base de datos
        db_path = os.path.join(db_folder, "migrexel_db.db")

        # Verificar si la base de datos existe
        if not os.path.exists(db_path):
            MessageHandler.show_info_message(
                self.ui,
                "Creando base de datos",
                f"La base de datos {db_path} no existe. Creando una nueva base de datos...",
                3000
            )
            try:
                # Crear la conexión
                conn = create_connection(db_path)

                # Crear tablas si no existen
                create_table_sql = """
                CREATE TABLE IF NOT EXISTS archivos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    ruta TEXT NOT NULL,
                    fecha_creacion TEXT NOT NULL
                );
                """
                execute_sql(conn, create_table_sql)

                # Cerrar la conexión
                conn.close()

                MessageHandler.show_success_message(
                    self.ui,
                    "Base de datos creada",
                    f"La base de datos {db_path} ha sido creada exitosamente.",
                    3000
                )
            except Exception as e:
                MessageHandler.show_error_message(
                    self.ui,
                    "Error",
                    f"No se pudo crear la base de datos: {e}",
                    3000
                )
        else:
            MessageHandler.show_info_message(
                self.ui,
                "Base de datos encontrada",
                f"La base de datos {db_path} ya existe.",
                3000
            )

    def show_context_menu_file_xls(self, position):
         # Obtener el índice del elemento en la posición del clic
        index = self.ui.listWidget_file_xls.indexAt(position)

        if not index.isValid():
            return  # No hay elemento válido en la posición del clic

        # Obtener el ítem seleccionado
        selected_item = self.ui.listWidget_file_xls.itemFromIndex(index)

        if selected_item is None:
            return  # No hay ítem seleccionado, no mostrar menú

        # Obtener la posición global del ratón
        global_position = self.ui.listWidget_file_xls.viewport().mapToGlobal(position)

        # Crear acciones para el menú
        actions = [
            {
                "text": "Eliminar",
                "callback": lambda: self.delete_file(selected_item),
                "icon": QIcon(":/icon/assets/icons/white/trash3-white.svg")  # Asegúrate de que el icono exista
            }
        ]

        # Mostrar el menú contextual
        self.context_menu_manager.create_context_menu(actions, global_position)

    def delete_file(self, item):
        # Obtener el nombre del archivo
        file_name = item.text()
        file_path = item.toolTip()

        # Mostrar un cuadro de diálogo de confirmación
        respuesta = QMessageBox.warning(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar el archivo '{file_name}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            try:
                # Eliminar el archivo de la carpeta archivos_xls
                os.remove(file_path)
                MessageHandler.show_success_message(
                    self.ui,
                    "Archivo eliminado",
                    f"El archivo '{file_name}' ha sido eliminado.",
                    3000
                )

                # Eliminar el ítem del QListWidget
                self.ui.listWidget_file_xls.takeItem(self.ui.listWidget_file_xls.row(item))

                # Actualizar la lista de tablas SQL si es necesario
                self.upload_sql()
            except Exception as e:
                MessageHandler.show_error_message(
                    self.ui,
                    "Error",
                    f"No se pudo eliminar el archivo: {e}",
                    3000
                )
   
    def show_context_menu_sql(self, position):
            # Obtener el índice del elemento en la posición del clic
            index = self.ui.listWidget_sql.indexAt(position)

            if not index.isValid():
                return  # No hay elemento válido en la posición del clic

            # Obtener el ítem seleccionado
            selected_item = self.ui.listWidget_sql.itemFromIndex(index)

            if selected_item is None:
                return  # No hay ítem seleccionado, no mostrar menú

            # Obtener la posición global del ratón
            global_position = self.ui.listWidget_sql.viewport().mapToGlobal(position)

            # Crear acciones para el menú
            actions = [
                {
                    "text": "Eliminar",
                    "callback": lambda: self.delete_table(selected_item),
                    "icon": QIcon(":/icon/assets/icons/white/trash3-white.svg")  # Asegúrate de que el icono exista
                }
            ]

            # Mostrar el menú contextual en la posición global
            self.context_menu_manager.create_context_menu(actions, global_position)

    def delete_table(self, item):
            # Obtener el nombre de la tabla
        table_name = item.text()

            # Mostrar un cuadro de diálogo de confirmación
        respuesta = QMessageBox.warning(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar la tabla '{table_name}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            try:
                    # Ruta a la base de datos
                db_path = os.path.join(os.getcwd(), "database", "migrexel_db.db")

                    # Conectar a la base de datos
                conn = create_connection(db_path)

                    # Ejecutar la sentencia DROP TABLE
                drop_table_sql = f'DROP TABLE "{table_name}";'
                execute_sql(conn, drop_table_sql)

                    # Cerrar la conexión
                conn.close()

                    # Eliminar el ítem del QListWidget
                self.ui.listWidget_sql.takeItem(self.ui.listWidget_sql.row(item))

                    # Mostrar un mensaje de éxito
                MessageHandler.show_success_message(
                    self.ui,
                    "Tabla eliminada",
                    f"La tabla '{table_name}' ha sido eliminada.",
                    3000
                )
            except Exception as e:
                    # Manejar errores
                MessageHandler.show_error_message(
                    self.ui,
                    "Error",
                    f"No se pudo eliminar la tabla: {e}",
                    3000
                )       
   
    def load_list_files(self):
        carpeta = os.path.join(os.getcwd(), "archivos_xls")
        if not os.path.exists(carpeta):
            MessageHandler.show_warning_message(
                self.ui,  "Carpeta no encontrada", f"La carpeta {carpeta} no existe.", 800
            )
            return

        archivos = os.listdir(carpeta)
        archivos_xls = [archivo for archivo in archivos if archivo.endswith(('.xls', '.xlsx'))]

        self.ui.listWidget_file_xls.clear()  # Limpiar la lista antes de agregar nuevos elementos

        for archivo in archivos_xls:
            item = QListWidgetItem(archivo)
            item.setToolTip(os.path.join(carpeta, archivo))  # Mostrar la ruta completa en el tooltip
            self.ui.listWidget_file_xls.addItem(item)

    def convert_sql(self):
        # Obtener el ítem seleccionado en el QListWidget
        selected_item = self.ui.listWidget_file_xls.currentItem()

        # Verificar si hay un ítem seleccionado
        if selected_item is None:
            MessageHandler.show_warning_message(
                self,  # Usar self como padre
                "Ningún archivo seleccionado",
                "Por favor, selecciona un archivo de la lista.",
                3000  # timeout
            )
            return

        # Obtener el nombre del archivo seleccionado
        file_name = selected_item.text()
        print(f"Archivo seleccionado: {file_name}")  # Mensaje de depuración

        # Obtener la ruta completa del archivo usando el tooltip (o construyéndola)
        file_path = selected_item.toolTip()  # Esto debería contener la ruta completa
        print(f"Ruta del archivo: {file_path}")  # Mensaje de depuración

        # Aquí puedes trabajar con el archivo seleccionado
        try:
            # Leer el archivo Excel
            self.ui.lbl_description.setText(f"Procesando archivo: {file_name}...")
            df = read_excel(file_path)
            if df is None:
                MessageHandler.show_error_message(
                    self,
                    "Error",
                    f"No se pudo leer el archivo Excel: {file_name}.",
                    3000
                )
                return

            # Mostrar un cuadro de diálogo para obtener el nombre de la tabla
            table_name, ok = QInputDialog.getText(
                self,
                "Nombre de la tabla",
                f"Ingrese el nombre de la tabla para el archivo {file_name}:"
            )
            if not ok or not table_name.strip():
                MessageHandler.show_warning_message(
                    self,
                    "Nombre de la tabla no ingresado",
                    "No se ha ingresado un nombre de tabla válido.",
                    3000
                )
                return
            sanitized_table_name = sanitizar_identificador(table_name.strip())

            # Generar el SQL para crear la tabla
            create_table_sql = generate_create_table_sql(df, sanitized_table_name)
            print(f"SQL para crear la tabla: {create_table_sql}")  # Mensaje de depuración

            # Conectar a la base de datos y crear la tabla
            db_path = os.path.join(os.getcwd(), "database", "migrexel_db.db")
            conn = create_connection(db_path)
            execute_sql(conn, create_table_sql)

            # Generar el SQL para insertar los datos
            insert_sql_statements = generate_insert_sql(df, sanitized_table_name)
            print(f"SQL para insertar datos: {len(insert_sql_statements)} sentencias.")  # Mensaje de depuración

            # Ejecutar las sentencias SQL para insertar los datos
            for insert_sql in insert_sql_statements:
                execute_sql(conn, insert_sql)
                print(f"Ejecutando: {insert_sql}")  # Mensaje de depuración

            # Guardar las sentencias SQL en un archivo
            sql_folder = os.path.join(os.getcwd(), "sql")
            os.makedirs(sql_folder, exist_ok=True)
            sql_file_path = os.path.join(sql_folder, f"{sanitized_table_name}.sql")
            with open(sql_file_path, "w", encoding="utf-8") as sql_file:
                sql_file.write(create_table_sql + "\n")
                for insert_sql in insert_sql_statements:
                    sql_file.write(insert_sql + "\n")
            print(f"Sentencias SQL guardadas en {sql_file_path}")  # Mensaje de depuración

            # Cerrar la conexión
            conn.close()

            # Finalizar
            self.ui.lbl_description.setText(f"Conversión de {file_name} completada.")
            MessageHandler.show_success_message(
                self,  # Usar self como padre
                "Conversión exitosa",
                f"El archivo {file_name} se ha convertido correctamente.",
                3000  # timeout
            )
            self.upload_sql()
        except Exception as e:
            # Manejar errores
            self.ui.lbl_description.setText(f"Error al procesar {file_name}.")
            MessageHandler.show_error_message(
                self,  # Usar self como padre
                "Error",
                f"Error al procesar el archivo {file_name}: {e}",
                3000  # timeout
            )

    def load_file(self):
        opciones, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo Excel",
            "",
            "Archivos Excel (*.xls *.xlsx);;Todos los archivos (*)"
        )

        if opciones:
            carpeta_destino = os.path.join(os.getcwd(), "archivos_xls")
            os.makedirs(carpeta_destino, exist_ok=True)
            nombre_archivo = os.path.basename(opciones)
            destino = os.path.join(carpeta_destino, nombre_archivo)

            try:
                with open(opciones, 'rb') as f_src:
                    with open(destino, 'wb') as f_dest:
                        f_dest.write(f_src.read())
                MessageHandler.show_success_message(
                    self.ui,  # ui
                    "Archivo Cargado",  # title
                    f"Archivo guardado en {destino}.",  # message
                    800  # timeout
                )
                self.load_list_files()  # Refrescar la lista de archivos
            except Exception as e:
               MessageHandler.show_error_message(
                    self.ui,  # ui
                    "Error",  # title
                    f"Error al guardar el archivo: {e}",  # message
                    800  # timeout
                )

    def upload_sql(self):
        # Ruta a la base de datos
        db_path = os.path.join(os.getcwd(), "database", "migrexel_db.db")

        # Verificar si la base de datos existe
        if not os.path.exists(db_path):
            MessageHandler.show_warning_message(
                self.ui,
                "Base de datos no encontrada",
                f"La base de datos {db_path} no existe.",
                3000
            )
            return

        try:
            # Conectar a la base de datos
            conn = create_connection(db_path)

            # Consultar las tablas
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            tables = cursor.fetchall()

            # Cerrar la conexión
            conn.close()

            # Limpiar el QListWidget antes de agregar nuevos elementos
            self.ui.listWidget_sql.clear()

            # Agregar las tablas al QListWidget
            for table in tables:
                table_name = table[0]
                item = QListWidgetItem(table_name)
                item.setToolTip(f"Tabla: {table_name}")  # Mostrar el nombre de la tabla en el tooltip
                self.ui.listWidget_sql.addItem(item)

            # Mostrar un mensaje de éxito
            MessageHandler.show_info_message(
                self.ui,
                "Tablas cargadas",
                "Las tablas se han cargado correctamente en la lista.",
                3000
            )
        except Exception as e:
            # Manejar errores
            MessageHandler.show_error_message(
                self.ui,
                "Error",
                f"No se pudieron cargar las tablas: {e}",
                3000
            )

    def search_row(self):
        # Implementa la lógica para search_row
        texto_busqueda = self.ui.search_input.text()
        self.ui.lbl_description.setText(f"Buscando: {texto_busqueda}")
        # Implementa tu lógica aquí
        self.ui.lbl_description.setText("Búsqueda completada.")

    def edit_data(self):
        # Implementa la lógica para modificar datos
        self.ui.lbl_description.setText("Modificando datos...")
        # Implementa tu lógica aquí
        self.ui.lbl_description.setText("Modificación completada.")

    def load_styles(self):
        ruta_qss = os.path.join(os.getcwd(), "theme", "dark.qss")

        if not os.path.exists(ruta_qss):
            QMessageBox.critical(self, "Error", f"No se encontró el archivo de estilos: {ruta_qss}")
            return

        try:
            with open(ruta_qss, "r") as archivo_qss:
                estilos = archivo_qss.read()
                self.setStyleSheet(estilos)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los estilos: {e}")

    def load_table_sql(self):
        # Ruta a la base de datos
        db_path = os.path.join(os.getcwd(), "database", "migrexel_db.db")

        # Verificar si la base de datos existe
        if not os.path.exists(db_path):
            MessageHandler.show_warning_message(
                self.ui,
                "Base de datos no encontrada",
                f"La base de datos {db_path} no existe.",
                3000
            )
            return

        try:
            # Conectar a la base de datos
            conn = create_connection(db_path)

            # Consultar las tablas
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            tables = cursor.fetchall()

            # Cerrar la conexión
            conn.close()

            if not tables:
                MessageHandler.show_warning_message(
                    self.ui,
                    "No hay tablas",
                    "No hay tablas en la base de datos para cargar.",
                    3000
                )
                return

            # Mostrar un cuadro de diálogo para seleccionar una tabla
            table_names = [table[0] for table in tables]
            table_selected, ok = QInputDialog.getItem(
                self,
                "Seleccionar tabla",
                "Seleccione la tabla que desea cargar:",
                table_names,
                editable=False
            )

            if not ok or not table_selected:
                return  # El usuario canceló la selección o no seleccionó una tabla

            # Establecer el nombre de la tabla actual
            self.current_table_name = table_selected

            # Conectar a la base de datos nuevamente para consultar la tabla
            conn = create_connection(db_path)
            cursor = conn.cursor()
            query = f'SELECT * FROM "{table_selected}";'
            cursor.execute(query)
            rows = cursor.fetchall()

            # Obtener los nombres de las columnas
            cursor.execute(f'PRAGMA table_info("{table_selected}");')
            columns_info = cursor.fetchall()
            column_names = [info[1] for info in columns_info]

            # Cerrar la conexión
            conn.close()

            # Configurar el QTableView con un modelo
            model = QStandardItemModel(len(rows), len(column_names))
            model.setHorizontalHeaderLabels(column_names)

            for row_index, row in enumerate(rows):
                for column_index, value in enumerate(row):
                    item = QStandardItem(str(value))
                    model.setItem(row_index, column_index, item)

            # Crear un proxy para el modelo
            self.proxy_model = QSortFilterProxyModel()
            self.proxy_model.setSourceModel(model)
            self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)  # Filtrado insensible a mayúsculas/minúsculas
            self.proxy_model.setFilterKeyColumn(-1)  # Filtrar en todas las columnas

            # Conectar el evento de texto cambiado en search_input
            self.ui.search_input.textChanged.connect(self.proxy_model.setFilterFixedString)

            # Establecer el modelo proxy en el QTableView
            self.ui.tableView_data.setModel(self.proxy_model)

            # Ajustar el tamaño de las columnas al contenido
            self.ui.tableView_data.resizeColumnsToContents()

            # Mostrar un mensaje de éxito
            MessageHandler.show_info_message(
                self.ui,
                "Tabla cargada",
                f"La tabla '{table_selected}' se ha cargado en la vista de datos.",
                3000
            )
        except Exception as e:
            # Manejar errores
            MessageHandler.show_error_message(
                self.ui,
                "Error",
                f"No se pudo cargar la tabla: {e}",
                3000
            )
    
    def keyPressEventOverride(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.print_selected_row()
        else:
            super().keyPressEvent(event)

    def print_selected_row(self):
        # Obtener el índice del elemento seleccionado
        selected_indexes = self.ui.tableView_data.selectionModel().selectedRows()
        if not selected_indexes:
            MessageHandler.show_warning_message(
                self.ui,
                "Ningún registro seleccionado",
                "Por favor, selecciona un registro para imprimir.",
                3000
            )
            return

        proxy_index = selected_indexes[0]
        source_index = self.proxy_model.mapToSource(proxy_index)
        row = source_index.row()

        # Obtener los datos actuales del modelo
        row_data = []
        for column in range(self.model.columnCount()):
            item = self.model.item(row, column)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append("")
        print(f"Datos de la fila seleccionada: {row_data}")
            
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()