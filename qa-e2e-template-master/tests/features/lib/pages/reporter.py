from pathlib import Path
import os
from datetime import datetime
class Reporter:
    def __init__(self):
        self.date = datetime.now().date()
        self.time = datetime.now().time()
        p = str(Path(__file__).parent)
        i = p.index("\\tests")
        self.new_dir = p[:i]+f"\\bug-reports\\log({self.date}).txt"
    def add_log(self, message):
        with open(os.path.join(self.new_dir), "a") as bug:
            bug.write(f"[{self.time}]: {message}"+"\n")
            bug.close()
