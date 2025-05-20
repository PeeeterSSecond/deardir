from deardir import DearDir
from pathlib import Path
import time

"""Test the DearDir class with a specific schema and root path."""

""" To Test CLI cd to this directory and run:
    deardir
    deardir --help
    deardir --version
    deardir check ./Tests --schema schema.yaml 
    deardir check ./Tests --schema schema.yaml --create
    ASYNC LIVE WATCHER:
    deardir watch ./Tests --schema schema.yaml --create --interval 1 --duration 10
"""

root_path = Path(__file__).parent / "Testdir"


aaschema = ["2", "3", [ {"4": ["a", "b"]}, {"5": ["c", "d"]}], ["a", "b"]] # ["a", "b"] -> Ok, ["a", ["b", "c"]] -> Error
aa = DearDir(root_paths=[root_path], schema=aaschema)
aa.create_missing = True
aa.validate()
print(aa)


schema = Path(__file__).parent / "schema.yaml"
dd = DearDir(root_paths=[root_path], schema=schema)
dd.create_missing = False
dd.validate()
print(dd)

thread = dd.live(3, 21, 2)
time.sleep(3)
dd.stop_live()
time.sleep(3)
dd.create_missing = True
dd.validate()
print(dd)
