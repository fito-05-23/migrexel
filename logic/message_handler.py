# core/utils/message_handler.py

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer, Qt, QSize
from PySide6.QtGui import QIcon, QPixmap

class MessageHandler:
    """Clase que centraliza los mensajes de la aplicación con estilos personalizados."""

    @staticmethod
    def show_message(ui, icon_type, title, message, timeout=3000):
        """Muestra un mensaje con un icono, título y texto personalizados."""
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)

        # Establecer el icono del mensaje
        if icon_type == "info":
            msg.setIcon(QMessageBox.Information)
            border_color_left = "#0b57d0"
            border_color = "#747474"
            button_color = "#0b57d0"
        elif icon_type == "warning":
            msg.setIcon(QMessageBox.Warning)
            border_color_left = "#efc765"
            border_color = "#747474"
            button_color = "#efc765"
        elif icon_type == "error":
            msg.setIcon(QMessageBox.Critical)
            border_color_left = "#ff0000"
            border_color = "#747474"
            button_color = "#ff0000"
        elif icon_type == "success":
            msg.setIcon(QMessageBox.Information)
            border_color_left = "#34a853"
            border_color = "#747474"
            button_color = "#34a853"
        else:
            msg.setIcon(QMessageBox.NoIcon)
            border_color = "#ffffff"
            button_color = "#ffffff"

        # Eliminar la barra de título
        msg.setWindowFlag(Qt.FramelessWindowHint)

        # Aplicar estilos personalizados
        msg.setStyleSheet(f"""
            QMessageBox {{
                background-color: rgb(24, 24, 24); /* Fondo azul oscuro */
                color: white !important; /* Texto blanco */
                font-size: 14px;
                border-top: 0.5px solid {border_color};
                border-right: 0.5px solid {border_color};
                border-left: 3px solid {border_color_left};
                border-bottom: 0.5px solid {border_color};
                padding: 10px;
                min-width: 500px; /* Ancho mínimo del mensaje */
            }}
            QMessageBox QLabel {{
                color: white !important;
            }}
            QMessageBox QPushButton {{
                background-color: {button_color};
                color: white !important; /* Texto blanco */
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }}
            QMessageBox QPushButton:hover {{
                background-color: {MessageHandler._adjust_color(button_color, 0x202020)};
            }}
        """)

        # Personalizar el icono
        icon_path = ""
        if icon_type == "info":
            icon_path = ":/icons/info_icon.png"
        elif icon_type == "warning":
            icon_path = ":/icons/warning_icon.png"
        elif icon_type == "error":
            icon_path = ":/icons/error_icon.png"
        elif icon_type == "success":
            icon_path = ":/icons/success_icon.png"

        if icon_path:
            icon = QIcon(QPixmap(icon_path))
            msg.setIconPixmap(icon.pixmap(QSize(32, 32)))

        # Mostrar el mensaje
        msg.exec()
        print("Mensaje mostrado")  # Mensaje de depuración


        # Cerrar el mensaje después de un tiempo si se especifica
        if timeout:
            QTimer.singleShot(timeout, msg.close)

    @staticmethod
    def _adjust_color(hex_color, adjustment):
        """Ajusta el color hexadecimal sumando un valor."""
        color = int(hex_color.lstrip('#'), 16)
        adjusted_color = min(max(color + adjustment, 0), 0xFFFFFF)
        return f"#{adjusted_color:06x}"

    @staticmethod
    def show_info_message(ui, title, message, timeout=3000):
        MessageHandler.show_message(ui, "info", title, message, timeout)

    @staticmethod
    def show_warning_message(ui, title, message, timeout=3000):
        MessageHandler.show_message(ui, "warning", title, message, timeout)

    @staticmethod
    def show_error_message(ui, title, message, timeout=3000):
        MessageHandler.show_message(ui, "error", title, message, timeout)

    @staticmethod
    def show_success_message(ui, title, message, timeout=3000):
        MessageHandler.show_message(ui, "success", title, message, timeout)