# search.py

from pathlib import Path


def search(root, keyword):
    """
    Search files and folders recursively.

    Args:
        root (str): Start directory.
        keyword (str): Search text.

    Returns:
        list: Matching paths.
    """

    results = []

    root = Path(root)

    if not root.exists():
        return results

    keyword = keyword.lower()

    try:
        for item in root.rglob("*"):

            if keyword in item.name.lower():

                results.append({
                    "name": item.name,
                    "path": str(item),
                    "type": "Folder" if item.is_dir() else "File"
                })

    except PermissionError:
        pass

    return results


def search_extension(root, extension):

    results = []

    root = Path(root)

    extension = extension.lower()

    for item in root.rglob("*"):

        if item.is_file() and item.suffix.lower() == extension:
            results.append(str(item))

    return results


def search_size(root, minimum_bytes):

    results = []

    root = Path(root)

    for item in root.rglob("*"):

        if item.is_file():

            try:
                if item.stat().st_size >= minimum_bytes:
                    results.append(str(item))
            except:
                pass

    return results