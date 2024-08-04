import sys
import ctypes
import winreg as reg
from PyQt6.QtWidgets import QMessageBox


def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()


def add_to_context_menu():
    try:
        reg_path = r"SystemFileAssociations\.zip\shell\OpenWithExtractHere"
        command = f'"{sys.executable}" "%1"'

        try:
            key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, reg_path, 0, reg.KEY_READ)
            reg.CloseKey(key)
            QMessageBox.information(None, "Failed", "Context menu entry for ExtractHere already exists.")
            return
        except FileNotFoundError:
            pass

        key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, reg_path)
        reg.SetValue(key, "", reg.REG_SZ, "Extract here")

        command_key = reg.CreateKey(key, "command")
        reg.SetValue(command_key, "", reg.REG_SZ, command)

        reg.CloseKey(key)
        reg.CloseKey(command_key)

        QMessageBox.information(None, "Success", "Successfully added ExtractHere to context menu for ZIP files.")

    except PermissionError:
        print("PermissionError: Administrative privileges are required to add context menu entry.")
    except Exception as e:
        QMessageBox.information(None, "Failed", {e})


def remove_from_context_menu():
    try:
        reg_path = r"SystemFileAssociations\.zip\shell\OpenWithExtractHere"

        try:
            key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, reg_path, 0, reg.KEY_READ)
            reg.CloseKey(key)
        except FileNotFoundError:
            QMessageBox.information(None, "Failed", "Context menu entry for ExtractHere does not exist.")
            return

        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, f"{reg_path}\\command")
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, reg_path)

        QMessageBox.information(None, "Success", "Successfully removed ExtractHere from context menu for ZIP files.")

    except PermissionError:
        print("PermissionError: Administrative privileges are required to remove context menu entry.")
    except Exception as e:
        QMessageBox.information(None, "Failed", {e})
