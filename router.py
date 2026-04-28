import time
import shutil
from pathlib import Path
from config import ROUTING_TABLE

def is_stable(path):
    try:
        file_size = path.stat().st_size
        time.sleep(2)
        return path.stat().st_size == file_size
    except FileNotFoundError:
        return False

def resolve_dest(dest_folder, name):
    candidate = dest_folder / name
    counter = 1
    p = Path(name)
    while candidate.exists():
        candidate = dest_folder / f"{p.stem}_{counter}{p.suffix}"
        counter += 1
    return candidate

def route_file(path):
    ext = path.suffix.lower()
    dest_folder = ROUTING_TABLE.get(ext)

    if dest_folder is None:
        return False

    if is_stable(path):
        dest_folder.mkdir(parents = True, exist_ok = True)
        dest = resolve_dest(dest_folder, path.name)
        shutil.move(str(path), dest)
        return True

    return False
