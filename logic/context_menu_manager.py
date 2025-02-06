from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction, QIcon

class ContextMenuManager:
    """Clase para gestionar menús contextuales con estilos personalizados."""

    def __init__(self, parent=None):
        self.parent = parent  # Widget padre donde se usará el menú contextual

    def create_context_menu(self, actions, position):
        """Crea y muestra un menú contextual.

        Args:
            actions: Una lista de diccionarios, donde cada diccionario define una acción:
                     {"text": "Texto de la acción", "callback": función_a_ejecutar, "icon": "ruta_al_icono"}
            position: QPoint donde se mostrará el menú.

        Returns:
            None
        """

        menu = QMenu(self.parent)

        for action_data in actions:
            action = QAction(action_data["text"], menu)
            if "icon" in action_data:
                action.setIcon(QIcon(action_data["icon"]))  # Asigna el icono si se proporciona
            action.triggered.connect(action_data["callback"])  # Conecta la señal triggered al callback
            menu.addAction(action)

        menu.setStyleSheet(""" 
            QMenu {
                background-color: rgb(24, 24, 24);
                color: white;
                border: 1px solid #5d5d5d;
                padding: 5px;
            }
            QMenu::item {
                background-color: rgb(24, 24, 24);
                color: white;
                padding: 5px 20px;
            }
            QMenu::item:selected {
                background-color: #333;
            }
            QMenu::icon {
                padding: 0px 8px; /* Ajusta el padding para el texto y el icono */
            }
            QAction {
                padding: 2px 5px;
            }
            QMenu::separator {
                height: 1px;
                background: #5d5d5d;
                margin: 5px 0;
            }
        """)

        menu.exec(position)