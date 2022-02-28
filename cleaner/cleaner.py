import os, argparse
from pathlib import Path


parser = argparse.ArgumentParser(description='Remove empty folders from a directory')
parser.add_argument('BASE_DIR', help='Directory to remove empty folders from')
parser.add_argument('-f', '--filter', help='Only remove folders matching filter', required=False)


def index(base_dir: str) -> list[Path]:
    """
    Indexes the directory and returns a list of all the empty files
    """
    empty_folders = []
    for root, dirnames, filenames in os.walk(base_dir):
        if not filenames and not dirnames:
            empty_folders.append(Path(root))
    
    return empty_folders


def filter_by_name(empties: list[Path], name_filter: str) -> list[Path]:
    return [e for e in empties if name_filter == e.name]


def prep(base_dir: str, name_filter: str=None):
    empties = index(base_dir)
    if name_filter:
        empties = filter_by_name(empties, name_filter)
    return empties


def clean(empties: list[Path]):    
    print("Starting Deletion...")
    for e in empties:
        print(f"Deleting {e}")
        e.rmdir()
    
    print("Done")


def main(base_dir: str, name_filter: str=None):
    empties = prep(base_dir, name_filter)

    print("Empty folders:")
    for e in empties:
        print(e)
    
    i = input(f"This will delete {len(empties)} empty folders, continue? (y/n): ")
    if i.lower() != 'y':
        print("Aborting")
        return
    else:
        clean(empties)

if __name__ == '__main__': # pragma: no cover
    args = parser.parse_args()
    base_dir = args.BASE_DIR
    name_filter = args.filter
    main(base_dir, name_filter)