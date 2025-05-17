from deardir import DearDir
from pathlib import Path

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
schema = Path(__file__).parent / "schema.yaml"

dd = DearDir(root_paths=[root_path], schema=schema)
dd.create_missing = True
dd.validate()