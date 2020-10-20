from pathlib import Path


class Site:
    def __init__(self, source, dest, parsers=None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []

    def create_dir(self, path):
        # Defining the path of the directory where the first part of the path
        # is the path of the destination path and the second part is the path
        # relative to source path
        directory = self.dest / path.relative_to(self.source)

        # Creating a folder. If a folder already exists, replacing it with a
        # new folder
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        # Creating a folder in the destination path. If a folder already
        # exists, replacing it with a new folder in the same path
        self.dest.mkdir(parents=True, exist_ok=True)

        # Iterate through the paths of source. If the path fetched is a
        # directory, create a directory at the current path.
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
