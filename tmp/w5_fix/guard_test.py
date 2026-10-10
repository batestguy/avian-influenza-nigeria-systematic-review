import sys
sys.path.insert(0, ".")
import build_figures as bf
out = bf.OUT / "validation_table.txt"
mtime_before = out.stat().st_mtime
bf.EXPECTED["E1"] = 999          # force a count mismatch
try:
    bf.main()
    print("GUARD TEST: FAIL - main() returned without aborting")
except SystemExit as e:
    print("GUARD TEST: SystemExit ->", str(e)[:90])
print("validation_table.txt mtime unchanged after failed guard:", out.stat().st_mtime == mtime_before)
