# -*- coding: utf-8 -*-

# An advanced setup script to create multiple executables and demonstrate a few
# of the features available to setup scripts
#
# hello.py is a very simple 'Hello, world' type script which also displays the
# environment in which the script runs
#
# Run the build process by running the command 'python setup_.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

import sys
from cx_Freeze import setup, Executable

base = 'Console'
if sys.platform == 'win32':
    base = 'Win32GUI'
options = {
    'build_exe': {
        'includes': [
            'show_demo_image',
            'create_menu',
            'cam_open'
        ],
        'path': sys.path
    }
}
executables = [
    Executable('gui_for_captcha.py',base=base),
    # Executable('Modulation_package.py',base=base),
    #Executable('create_menu.py',base=base)
]

setup(name='main_frame',
      version='0.1',
      description='Advanced sample cx_Freeze script',
      #options=options,
      executables=executables
      )