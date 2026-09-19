from pathlib import Path
import os

targets = [
    r"C:\Windows",
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    r"C:\ProgramData",
    r"C:\Users\TOSHIBA",
    r"C:\Python314",
    r"C:\conda-envs",
    r"C:\Repos",
    r"C:\Temp",
    r"C:\tmp",
]

def scan(root):
    total = 0
    files = []
    dirs = 0
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
                            size = entry.stat(follow_symlinks=False).st_size
                            total += size
                            files.append((size, entry.path))
                        elif entry.is_dir(follow_symlinks=False):
                            dirs += 1
                            stack.append(Path(entry.path))
                    except (OSError, PermissionError):
                        continue
        except (OSError, PermissionError):
            continue
    return total, dirs, sorted(files, reverse=True)

def gb(value):
    return value / (1024 ** 3)

drive = os.statvfs("C:\\") if hasattr(os, "statvfs") else None
print("=== C DRIVE ===")
if drive:
    total = drive.f_blocks * drive.f_frsize
    free = drive.f_bavail * drive.f_frsize
    print(f"TotalGB={gb(total):.2f} FreeGB={gb(free):.2f} UsedGB={gb(total-free):.2f}")
else:
    import shutil
    total, used, free = shutil.disk_usage("C:\\")
    print(f"TotalGB={gb(total):.2f} FreeGB={gb(free):.2f} UsedGB={gb(used):.2f}")

print("=== TARGET FOLDER TOTALS ===")
all_files = []
for target in targets:
    if not os.path.exists(target):
        continue
    print(f"Scanning {target}", flush=True)
    size, dirs, files = scan(target)
    all_files.extend(files)
    print(f"{size/(1024**3):.2f} GB\t{size/(1024**2):.0f} MB\t{dirs} dirs\t{target}")

print("=== TOP 30 FILES IN SCANNED LOCATIONS ===")
for size, path in sorted(all_files, reverse=True)[:30]:
    print(f"{size/(1024**3):.2f} GB\t{size/(1024**2):.0f} MB\t{path}")
