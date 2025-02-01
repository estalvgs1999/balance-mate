import os
import shutil

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFileDialog, QMainWindow, QVBoxLayout, QWidget

from ui.components.file_selector import FileSelector
from ui.components.progress_bar import ProgressBar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BalanceMate")
        self.setFixedSize(400, 200)

        # Set window icon
        self.setWindowIcon(QIcon("resources\icons\icon.png"))
        # Layout principal
        self.layout = QVBoxLayout()

        # Componente de selección de archivo
        self.file_selector = FileSelector(self.handle_file)
        self.layout.addWidget(self.file_selector)

        # Barra de progreso
        self.progress_bar = ProgressBar()
        self.layout.addWidget(self.progress_bar)

        # Contenedor principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def handle_file(self, file_path):
        from core.validator import validate_csv_structure
        from ui.report_window import ReportWindow

        if validate_csv_structure(file_path):
            self.report_window = ReportWindow(file_path, self.start_processing)
            self.report_window.show()
        else:
            from ui.components.message_box import show_error

            show_error(
                self,
                "Estructura inválida",
                "El archivo CSV no tiene la estructura esperada.",
            )

    def start_processing(self, file_path, month, year):
        from core.processor import FileProcessor

        self.progress_bar.setVisible(True)
        self.progress_bar.reset()

        self.processor = FileProcessor(file_path, month, year)
        self.processor.progress.connect(self.progress_bar.update_progress)
        self.processor.finished.connect(self.processing_finished)
        self.processor.start()

    def processing_finished(self, success, message, output_file_path):
        self.progress_bar.setVisible(False)
        from ui.components.message_box import show_error, show_info

        if success:
            suggested_name = os.path.basename(output_file_path)
            save_path, _ = QFileDialog.getSaveFileName(
                self, "Save File", suggested_name, "Excel Files (*.xlsx)"
            )
            if save_path:
                try:
                    shutil.move(output_file_path, save_path)
                    show_info(self, "Success", "File saved successfully.")

                except Exception as e:
                    show_error(self, "Error", f"Error saving file: {str(e)}")
            else:
                show_error(self, "Error", message)
