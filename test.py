import threading
import time
import sys

class ProgressBar:
    def __init__(self, total):
        self.total = total
        self.progress = 0

    def update(self):
        self.progress += 1
        sys.stdout.write("\r[%-20s] %d%%" % ('=' * int(self.progress / self.total * 20), self.progress / self.total * 100))
        sys.stdout.flush()

def my_function(progress_bar):
    for i in range(100):
        time.sleep(0)
        progress_bar.update()

if __name__ == "__main__":
    progress_bar = ProgressBar(100)
    thread = threading.Thread(target=my_function, args=(progress_bar,))
    thread.start()
    thread.join()