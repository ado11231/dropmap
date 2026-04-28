from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import WATCHING_FOLDER
import router

class Handler(FileSystemEventHandler):
    def __init__(self, file_router):
        self.file_router = file_router

    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)

        if path.suffix in (".crdownload", ".part"):
            return
        self.file_router.route_file(path)

def folder_observer():
    handler = Handler(file_router=router)
    observer = Observer()
    observer.schedule(handler, str(WATCHING_FOLDER), recursive = False)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(timeout=1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_observer()
