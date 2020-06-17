from pathlib import Path, PurePath
import os
from os import mkdir


class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest + "/" + PurePath.relative_to(path)
        mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        mkdir(self.dest, parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if os.path.isdir(path):
                self.create_dir(path)
