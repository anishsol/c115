import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        source_file_path = os.path.join(event.src_path, "main.txt")
        destination_file_path = os.path.join(event.src_path, "backup", "main_backup.txt")

        if os.path.exists(source_file_path):
            # Handle modified event here
            print(f'File {source_file_path} has been modified. Moving to {destination_file_path}')
            os.rename(source_file_path, destination_file_path)
        else:
            print(f'File {source_file_path} does not exist.')

if __name__ == "__main__":
    path_to_watch = "F:/1aa/coding/python projects/c115"  # Change this to the directory you want to monitor

    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)

    print(f"Monitoring changes in {path_to_watch}. Press Ctrl+C to stop.")
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
