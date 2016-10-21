# Ticket Modifier
# Version v1.1
# Copyright © 2016 AboodXD

import os, shutil, sys
from cx_Freeze import setup, Executable

version = '1.1'

# Pick a build directory
dir_ = 'tik_modifier v' + version

# Add the "build" parameter to the system argument list
if 'build' not in sys.argv:
    sys.argv.append('build')

# Clear the directory
print('>> Clearing/creating directory...')
if os.path.isdir(dir_): shutil.rmtree(dir_)
os.makedirs(dir_)
print('>> Directory ready!')

setup(
    name = 'Ticket Modifier',
    version = version,
    description = 'Wii U Ticket Modifier',
    author = "AboodXD",
    options={
        'build_exe': {
            'compressed': 1,
            'build_exe': dir_,
            },
        },
    executables = [
        Executable(
            'tik_modifier.py',
            ),
        ],
    )

print('>> Attempting to copy required files...')
shutil.copy('README.md', dir_)
print('>> Files copied!')

print('>> Ticket Modifier has been frozen to "%s"!' % dir_)
