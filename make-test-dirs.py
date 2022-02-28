import os, shutil
from pathlib import Path
from random import randint

base_path = Path(os.getcwd()) / "tmp"

shutil.rmtree(base_path, ignore_errors=True)

base_path.mkdir()

for i in range(400):
    (base_path / f"dir{i}").mkdir()
    match randint(0, 2):
        case 1:
            (base_path / f"dir{i}" / "file").touch()
        case 2:
            (base_path / f"dir{i}" / "subdir").mkdir()
            if randint(0, 1) == 1:
                (base_path / f"dir{i}" / "subdir" / "file").touch()