from cx_Freeze import setup, Executable

executables = [
    Executable('extract_here.py', base='Win32GUI')  # Replace 'file.py' with your script name and 'icon.ico' with your icon file
]

setup(name='Extract herer',
      version='1.0',
      executables=executables)
