import json
from pathlib import Path


def test_all_json_files_are_valid():
    root_dir = Path(__file__).resolve().parents[1]
    json_files = list(root_dir.glob('*.json'))
    assert json_files, 'No JSON files found to validate.'

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            try:
                json.load(f)
            except json.JSONDecodeError as e:
                raise AssertionError(f"{json_file} is not valid JSON: {e}")
