from pathlib import Path
from ssg.parsers import Parser


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
            elif path.is_dir():
                self.run_parser(path)

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            print("Not Implemented")
