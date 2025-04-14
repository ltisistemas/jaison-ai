# watcher.py
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher(FileSystemEventHandler):
    def __init__(self):
        self.process = subprocess.Popen(["python", "main.py"])

    def on_modified(self, event):
        if event.src_path.endswith("main.py"):
            print("🌀 Arquivo modificado, reiniciando...")
            self.process.kill()
            time.sleep(0.5)
            self.process = subprocess.Popen(["python", "main.py"])

if __name__ == "__main__":
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)

    try:
        observer.start()
        print("👀 Observando mudanças em main.py...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        event_handler.process.kill()
    observer.join()
