from pathlib import Path
import os

parents = [
    Path(r"C:\Users\TOSHIBA\AppData\Local"),
    Path(r"C:\Users\TOSHIBA\miniconda3\envs"),
    Path(r"C:\Users\TOSHIBA\.codex"),
    Path(r"C:\Users\TOSHIBA\.local\share"),
    Path(r"C:\Users\TOSHIBA\.cmdstan"),
]

def scan(root):
    total = 0
    stack = [root]
    while stack:
        current = stack.pop()
        try:
            with os.scandir(current) as entries:
                for entry in entries:
                    try:
                        if entry.is_symlink():
                            continue
                        if entry.is_file(follow_symlinks=False):
                            total += entry.stat(follow_symlinks=False).st_size
                        elif entry.is_dir(follow_symlinks=False):
                            stack.append(Path(entry.path))
                    except (OSError, PermissionError):
                        continue
        except (OSError, PermissionError):
            continue
    return total

for parent in parents:
    print(f"=== {parent} ===")
    if not parent.exists():
        continue
    rows = []
    for child in parent.iterdir():
        if child.is_symlink():
            continue
        if child.is_dir():
            rows.append((scan(child), str(child)))
        elif child.is_file():
            rows.append((child.stat().st_size, str(child)))
    for size, path in sorted(rows, reverse=True)[:20]:
        print(f"{size/(1024**3):.2f} GB\t{size/(1024**2):.0f} MB\t{path}")
