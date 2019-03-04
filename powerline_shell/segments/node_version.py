import subprocess
from ..utils import ThreadedSegment


class Segment(ThreadedSegment):
    def run(self):
        try:
            p1 = subprocess.Popen(["node", "--version"], stdout=subprocess.PIPE)
            self.version = p1.communicate()[0].decode("utf-8").rstrip()
        except OSError:
            self.version = None

    def add_to_powerline(self):
        self.join()
        if not self.version:
            return
        # FIXME no hard-coded colors
        self.powerline.append(" ⬢ ", 144, self.powerline.theme.NODE_BG, "")
        self.powerline.append(self.version, self.powerline.theme.NODE_FG, self.powerline.theme.NODE_BG)
