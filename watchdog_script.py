import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class MyHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.start_script()

    def start_script(self):
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen([sys.executable, self.script])
        print(Fore.GREEN + f"Started {self.script}")

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            print(Fore.YELLOW + f'{self.script} has been modified. Restarting...')
            self.start_script()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.RED + "Usage: python watchdog_script.py <script_to_watch.py>")
        sys.exit(1)

    script_to_watch = sys.argv[1]
    event_handler = MyHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    print(Fore.CYAN + f"Watching {script_to_watch} for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(Fore.RED + "Stopping observer...")
    observer.join()
