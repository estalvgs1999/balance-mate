import os
import sys
import winreg

from win32com.client import Dispatch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def get_reg(name: str, path: str) -> None:
    """Reads a value from the Windows Registry.

    Args:
            name (str): The name of the registry key to read.
            path (str): The path of the registry key.

    Returns:
            str: The value from the registry, or None if not found.
    """
    try:
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_READ
        )
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


def create_shortcut(
    link_name: str,
    script_relative_path: str,
    python_exe_path: str,
    icon_relative_path: str = None,
):
    """Creates a Windows shortcut to execute a Python script directly with an optional custom icon.

    Args:
            script_relative_path (str): The relative path to the Python script.
            python_exe_path (str): The absolute path to the Python interpreter.
            icon_relative_path (str, optional): The relative path to the icon file. Defaults to None.
    """
    # Get the absolute path for the script
    script_path = os.path.abspath(script_relative_path)

    # Name of the shortcut file (.lnk)
    script_name = os.path.basename(script_path)
    link_name = f"{link_name}.lnk"

    # Get the user's desktop folder from the Windows registry
    reg_name = "Desktop"
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    desktop_folder = os.path.normpath(get_reg(reg_name, reg_path))

    # Expand any environment variables in the path
    desktop_folder = os.path.expandvars(desktop_folder)

    # Full path to the shortcut file
    path_link = os.path.join(desktop_folder, link_name)

    # Ensure the desktop path is correct
    if not os.path.exists(desktop_folder):
        raise FileNotFoundError(f"The desktop path does not exist: {desktop_folder}")

    # Create the shortcut using Windows Script Host
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path_link)
    shortcut.Targetpath = python_exe_path  # Path to Python interpreter
    shortcut.Arguments = f'"{script_path}"'  # Pass the script as an argument
    shortcut.WorkingDirectory = os.path.dirname(script_path)

    # Set custom icon if provided
    if icon_relative_path:
        icon_path = os.path.abspath(icon_relative_path)
        if os.path.exists(icon_path):
            shortcut.IconLocation = icon_path
        else:
            raise FileNotFoundError(f"The icon path does not exist: {icon_path}")

    shortcut.save()


def main():
    """Main function to execute the script."""

    python_exe_path = os.path.join(os.getcwd(), ".venv", "Scripts", "pythonw.exe")
    script_relative_path = os.path.join(os.getcwd(), "main.pyw")
    icon_relative_path = os.path.join(os.getcwd(), "resources", "icons", "icon.ico")

    create_shortcut(
        "BalanceMate",
        str(script_relative_path),
        str(python_exe_path),
        str(icon_relative_path),
    )


if __name__ == "__main__":
    main()
