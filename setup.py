import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pygame"], "excludes": ["tkinter"], "include_files": ["ship.bmp"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Alien_Invasion",
        version = "0.1",
        description = "Aliens!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("alien_invasion.py", base=base)])