import pytest
from pathlib import Path
from deardir import DearDir

def test_add_existing_path(tmp_path):
    dd = DearDir()
    dd.add_path(tmp_path)
    assert tmp_path in dd.entitys

def test_add_missing_path_raises():
    dd = DearDir()
    with pytest.raises(FileNotFoundError):
        dd.add_path(Path("this/does/not/exist"))

def test_set_schema_from_dict():
    schema = {"src": ["main.py", {"utils": ["helpers.py"]}]}
    dd = DearDir()
    dd.set_schema(schema)
    assert isinstance(dd.schema, list)
    assert dd.schema[0]["src"][0] == "main.py"

def test_validate_finds_missing(tmp_path):
    schema = {"src": ["main.py"]}
    dd = DearDir(root_paths=[tmp_path], schema=schema)
    dd.validate()
    expected = tmp_path / "src" / "main.py"
    assert expected in dd.missing

def test_validate_creates_files(tmp_path):
    schema = {"data": ["example.txt"]}
    dd = DearDir(root_paths=[tmp_path], schema=schema)
    dd.create_missing = True
    dd.validate()
    created_file = tmp_path / "data" / "example.txt"
    assert created_file.exists()
    assert created_file in dd.created

def test_repr_output(tmp_path):
    dd = DearDir(root_paths=[tmp_path], schema={"src": []})
    out = repr(dd)
    assert "<DearDir>" in out
    assert "entitys" in out
