from pathlib import Path
import os

targets = [
    r"C:\Users\TOSHIBA\AppData\Local",
    r"C:\Users\TOSHIBA\AppData\Roaming",
    r"C:\Users\TOSHIBA\miniconda3",
    r"C:\Users\TOSHIBA\.local",
    r"C:\Users\TOSHIBA\.cmdstan",
    r"C:\Users\TOSHIBA\.cache",
    r"C:\Users\TOSHIBA\.codex",
    r"C:\Users\TOSHIBA\.docker",
    r"C:\Users\TOSHIBA\appdev-env",
    r"C:\Users\TOSHIBA\ds-general",
    r"C:\Users\TOSHIBA\data",
    r"C:\Users\TOSHIBA\datasets",
    r"C:\Users\TOSHIBA\Downloads",
    r"C:\Users\TOSHIBA\Documents",
    r"C:\Users\TOSHIBA\Desktop",
    r"C:\Users\TOSHIBA\OneDrive",
]

def scan(root):
    total = 0
    stack = [Path(root)]
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

print("=== PROFILE SUBFOLDER TOTALS ===")
for target in targets:
    if os.path.exists(target):
        size = scan(target)
        print(f"{size/(1024**3):.2f} GB\t{size/(1024**2):.0f} MB\t{target}")
