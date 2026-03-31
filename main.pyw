import ctypes
import os
import sys
import time

from PyQt6.QtWidgets import QApplication

from ui.main_window import MainWindow

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    # Set the application user model ID for Windows taskbar icon (Windows only)
    if sys.platform == "win32":
        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                "balance-mate.ealvarado.v1.0"
            )
            # Delay to ensure the ID is set
            time.sleep(1)
        except AttributeError:
            pass

    app = QApplication(sys.argv)
    
    # Apply modern styling
    style_path = resource_path(os.path.join("ui", "styles", "main.qss"))
    if os.path.exists(style_path):
        with open(style_path, "r") as f:
            app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
