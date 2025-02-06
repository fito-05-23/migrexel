from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt

class PreloadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Cargando...")
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color: rgb(24, 24, 24); color: white;")

        layout = QVBoxLayout()

        # Agregar un GIF de carga
        self.movie = QMovie(":/icon/assets/images/preload.gif")  # Asegúrate de que el GIF exista
        label = QLabel()
        label.setMovie(self.movie)
        self.movie.start()

        # Agregar un mensaje
        message = QLabel("Convirtiendo archivos, por favor espere...")
        message.setAlignment(Qt.AlignCenter)

        # Agregar espaciadores para centrar el contenido
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout.addSpacerItem(spacer)
        layout.addWidget(label)
        layout.addWidget(message)
        layout.addSpacerItem(spacer)

        self.setLayout(layout)