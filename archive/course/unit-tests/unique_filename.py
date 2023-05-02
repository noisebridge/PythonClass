import os
from pathlib import Path
from uuid import uuid1

def unique_filename(directory, filename):
    path = Path(filename)

    if filename in os.listdir(directory):
        return f'{path.stem}_{uuid1()}{path.suffix}'
    else:
        return str(path)
