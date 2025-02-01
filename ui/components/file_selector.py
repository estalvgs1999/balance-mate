from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt


class FileSelector(QWidget):
    def __init__(self, file_callback):
        super().__init__()
        self.file_callback = file_callback

        layout = QVBoxLayout()

        self.label = QLabel("Arrastra un archivo CSV aquí o selecciona uno.")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Seleccionar Archivo CSV")
        self.button.clicked.connect(self.select_file)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.file_callback(file_path)

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Seleccionar CSV", "", "Archivos CSV (*.csv)"
        )
        if file_path:
            self.file_callback(file_path)
