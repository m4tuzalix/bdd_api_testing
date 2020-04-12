from pathlib import Path
from datetime import datetime
class Reporter:
    def __init__(self):
        self.date = datetime.now().date()
        self.time = datetime.now().time()
    def add_log(self, message):
        with open(Path(f"/qa-e2e-template-master/bug-reports/log({self.date}).txt"), "a") as bug:
            bug.write(f"[{self.time}]: {message}"+"\n")
            bug.close()