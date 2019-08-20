import sys
from cx_Freeze import setup, Executable

# <added>
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
# </added>

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('launcher.py', base=base)
]

# <added>
options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            "core",
            "graphic",
            "file",
            "img",
            "shortcuts"
         ],
        'packages':[
            "bs4",
            "requests",
            "idna",
            "queue",
            "lxml"
        ]
    },
}
# </added>

setup(name = 'Launcher',
      version = '1.0',
      description = 'Lancer vos applis',
      url = 'https://github.com/quentinhouillon/launcher_interface',
      # <added>
      options = options,
      # </added>
      executables = executables
      )

# run: 'python setup.py build'
