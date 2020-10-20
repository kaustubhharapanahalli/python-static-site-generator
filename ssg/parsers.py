from typing import List
from pathlib import Path


class Parser:
    # Create an empty dictionary. Annotate the variable with the type of
    # List(str)
    extensions: List[str] = []

    def valid_extension(self, extension):
        # To validate if a file have a parser, check if the extension part of
        # the class extensions variable.
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
