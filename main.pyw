import ctypes
import sys
import time

from PyQt6.QtWidgets import QApplication

from ui.main_window import MainWindow


def main():
    # Set the application user model ID for Windows taskbar icon
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "balance-mate.ealvarado.v1.0"
    )

    # Delay to ensure the ID is set
    time.sleep(1)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
