from PyQt6.QtWidgets import QProgressBar


class ProgressBar(QProgressBar):
    def __init__(self):
        super().__init__()
        self.setVisible(False)
        self.setValue(0)

    def update_progress(self, value):
        self.setVisible(True)
        self.setValue(value)
