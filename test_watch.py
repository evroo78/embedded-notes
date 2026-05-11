import time
import sys
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Подія: Файл змінено! Шлях: {event.src_path}")
    def on_created(self, event):
        print(f"Подія: Створено новий файл! Шлях: {event.src_path}")

if __name__ == "__main__":
    path = "."  # стежити за поточною папкою
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    print(f"Старт моніторингу в папці: {path}")
    print("Змініть або створіть файл у цій папці...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()