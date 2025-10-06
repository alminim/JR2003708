import yaml
from typing import List, Union
from pathlib import Path
from .cell_occupant import Dragon, Princess


def read_input_from_file(input_file: Path) -> dict:
    if not input_file.exists() or input_file.is_dir():
        return {}
    return read_input(input_file.read_text())


def read_input(input_text: str) -> dict:
    try:
        loaded_data = yaml.safe_load(input_text)
    except yaml.YAMLError:
        loaded_data = {}
    return loaded_data


def validate_input(input: dict) -> bool:
    if not input or "num_cells" not in input or "cells" not in input:
        return False

    num_cells = input["num_cells"]
    cells = input["cells"]

    if type(num_cells) is not int or type(cells) is not list:
        return False

    if num_cells - 1 != len(cells):
        return False

    if num_cells < 2:
        return False

    return True


def parse_cells(cells: List[str]) -> List[Union[Dragon, Princess]]:
    parsed_cells = []

    for i, cell in enumerate(cells):
        cell_type, value = cell.split()
        try:
            value = int(value)
        except ValueError:
            return []

        if value < 1:
            return []

        if cell_type == "d":
            parsed_cells.append(Dragon(value, i))
        elif cell_type == "p":
            parsed_cells.append(Princess(value, i))
        else:
            return []

    if type(parsed_cells[-1]) is not Princess:
        return []
    return parsed_cells
