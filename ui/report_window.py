import os
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QComboBox, QHBoxLayout, QLabel, QPushButton,
                             QVBoxLayout, QWidget, QGraphicsDropShadowEffect)


class ReportWindow(QWidget):
    def __init__(self, file_path, process_callback):
        super().__init__()
        self.setWindowTitle("Select Month and Year")
        self.setFixedSize(350, 230)

        # Set window icon
        self.setWindowIcon(QIcon(os.path.join("resources", "icons", "icon.png")))

        self.file_path = file_path
        self.process_callback = process_callback

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        self.month_combo = QComboBox()
        self.month_combo.addItems(
            [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ]
        )
        layout.addWidget(QLabel("Select Month:"))
        layout.addWidget(self.month_combo)

        self.year_combo = QComboBox()
        self.year_combo.addItems([str(year) for year in range(2025, 2040)])
        layout.addWidget(QLabel("Select Year:"))
        layout.addWidget(self.year_combo)

        button_layout = QHBoxLayout()

        process_button = QPushButton("Convert")
        process_button.clicked.connect(self.start_processing)
        button_layout.addWidget(process_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def start_processing(self):
        month = self.month_combo.currentText()
        year = self.year_combo.currentText()
        self.process_callback(self.file_path, month, year)
        self.close()
