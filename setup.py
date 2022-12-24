from distutils.core import setup
import py2exe

#for creating a exe file from the script

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console=[{'script': "main.py"}],
    zipfile = None,
)