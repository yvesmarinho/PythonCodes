"""
    Teste de programa que monitora pasta e move arquivo
    funcionou corretamente
    https://www.youtube.com/watch?v=GKIJKgYpLpM

    TODO
        - adicionar logs
        -
"""

from watchdog import observers
from watchdog.events import FileSystemEventHandler
# import json
import os, time, shutil

Path_From = "C://Downloads//teste01"
Path_To = "C://Downloads//teste02"

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(Path_From):
            file_folder = os.path.join(Path_From, file)
            shutil.move(file_folder, Path_To)


event_handler = FileHandler()
observer = observers.Observer()
observer.schedule(event_handler, Path_From, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    observer.stop()

observer.join()