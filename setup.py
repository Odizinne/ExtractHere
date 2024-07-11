from cx_Freeze import setup, Executable

build_dir = "build/ExtractHere"

base = "Win32GUI"

target_name="extracthere.exe"

zip_include_packages = ['PyQt6', 'zipfile']

executables = [
    Executable('extract_here.py', base=base, target_name=target_name)
]

build_exe_options = {
    "build_exe": build_dir,
    "zip_include_packages": zip_include_packages,
    "excludes": ["tkinter", "PyQt5", "PySide6", "pygetwindow", "PyQt6-WebEngine", "numpy"],
}

setup(name='ExtractHere',
      version='1.0',
      options={"build_exe": build_exe_options},
      executables=executables)
