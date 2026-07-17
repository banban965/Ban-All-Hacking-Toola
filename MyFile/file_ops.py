# file_ops.py

import os
import shutil
from pathlib import Path
from datetime import datetime


def create_file(path, name):
    try:
        (Path(path) / name).touch(exist_ok=True)
        return True, "File created."
    except Exception as e:
        return False, str(e)


def create_folder(path, name):
    try:
        (Path(path) / name).mkdir(exist_ok=True)
        return True, "Folder created."
    except Exception as e:
        return False, str(e)


def delete(path):
    try:
        target = Path(path)

        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()

        return True, "Deleted."
    except Exception as e:
        return False, str(e)


def rename(path, new_name):
    try:
        p = Path(path)
        p.rename(p.parent / new_name)
        return True, "Renamed."
    except Exception as e:
        return False, str(e)


def copy(src, dst):
    try:
        src = Path(src)
        dst = Path(dst)

        if src.is_dir():
            shutil.copytree(src, dst / src.name)
        else:
            shutil.copy2(src, dst)

        return True, "Copied."
    except Exception as e:
        return False, str(e)


def move(src, dst):
    try:
        shutil.move(src, dst)
        return True, "Moved."
    except Exception as e:
        return False, str(e)


def info(path):
    try:
        p = Path(path)

        return {
            "Name": p.name,
            "Path": str(p),
            "Type": "Folder" if p.is_dir() else "File",
            "Size": p.stat().st_size,
            "Modified": datetime.fromtimestamp(
                p.stat().st_mtime
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "Readable": os.access(p, os.R_OK),
            "Writable": os.access(p, os.W_OK),
            "Executable": os.access(p, os.X_OK)
        }

    except Exception as e:
        return {"Error": str(e)}