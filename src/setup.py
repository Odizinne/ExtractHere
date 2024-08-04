import os
from cx_Freeze import setup, Executable

build_dir = "build/ExtractHere"
src_dir = os.path.dirname(os.path.abspath(__file__))

zip_include_packages = ["PyQt6", "zipfile"]

build_exe_options = {
    "build_exe": build_dir,
    "zip_include_packages": zip_include_packages,
    "excludes": ["tkinter"],
}

executables = [Executable(os.path.join(src_dir, "extract_here.py"), base="Win32GUI", target_name="ExtractHere")]

setup(name="ExtractHere", version="1.0", options={"build_exe": build_exe_options}, executables=executables)
