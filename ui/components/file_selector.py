from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt


class FileSelector(QWidget):
    def __init__(self, file_callback):
        super().__init__()
        self.file_callback = file_callback
        self.setObjectName("fileSelector")

        layout = QVBoxLayout()

        self.label = QLabel("Drag and drop a CSV file here, or select one.")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Select CSV File")
        self.button.clicked.connect(self.select_file)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setAcceptDrops(True)
        self.setProperty("dragActive", False)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            self.setProperty("dragActive", True)
            self.style().unpolish(self)
            self.style().polish(self)
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.setProperty("dragActive", False)
        self.style().unpolish(self)
        self.style().polish(self)

    def dropEvent(self, event):
        self.setProperty("dragActive", False)
        self.style().unpolish(self)
        self.style().polish(self)
        
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.file_callback(file_path)

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Select CSV", "", "CSV Files (*.csv)"
        )
        if file_path:
            self.file_callback(file_path)
