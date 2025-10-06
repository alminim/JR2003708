import unittest
from pathlib import Path
from src.input_reader import (
    read_input_from_file,
    read_input,
    validate_input,
    parse_cells,
)
from src.cell_occupant import Dragon, Princess


class TestInputReader(unittest.TestCase):
    def test_read_input_from_file(self):
        nonexisting_file = Path("/proc/fake_file")
        directory = Path(".")
        self.assertEqual(read_input_from_file(nonexisting_file), {})
        self.assertEqual(read_input_from_file(directory), {})

    def test_read_input(self):
        good_yaml = """
num_cells: 2
cells:
    - d 1
"""
        empty_text = ""

        self.assertEqual(read_input(good_yaml), {"num_cells": 2, "cells": ["d 1"]})
        self.assertEqual(read_input(empty_text), None)

    def test_validate_input(self):
        valid_input = {"num_cells": 2, "cells": ["d 1"]}
        missing_num_cells = {"cells": ["d 1"]}
        missing_cells = {"cells": ["d 1"]}
        wrong_num_cells = {"num_cells": 10, "cells": ["d 1"]}
        too_few_cells = {"num_cells": 0, "cells": []}
        wrong_num_cells_type = {"num_cells": "a", "cells": ["d 1"]}
        wrong_cells_type = {"num_cells": 2, "cells": "a"}

        self.assertTrue(validate_input(valid_input))

        self.assertFalse(validate_input(missing_num_cells))
        self.assertFalse(validate_input(missing_cells))
        self.assertFalse(validate_input(wrong_num_cells))
        self.assertFalse(validate_input(too_few_cells))
        self.assertFalse(validate_input(wrong_num_cells_type))
        self.assertFalse(validate_input(wrong_cells_type))

    def test_parse_celss(self):
        valid_input = ["d 1", "p 1"]
        last_cell_not_princess = ["d 1"]
        wrong_occupant_type = ["a 1"]
        bad_gold_value = ["d -1", "p 1"]
        bad_beauty_value = ["d 1", "p -1"]
        non_int_gold_value = ["d 1.5", "p 1"]
        non_int_beauty_value = ["d 1", "p 1.5"]

        self.assertEqual(parse_cells(valid_input), [Dragon(1, 0), Princess(1, 1)])

        self.assertEqual(parse_cells(last_cell_not_princess), [])
        self.assertEqual(parse_cells(wrong_occupant_type), [])
        self.assertEqual(parse_cells(bad_gold_value), [])
        self.assertEqual(parse_cells(bad_beauty_value), [])
        self.assertEqual(parse_cells(non_int_beauty_value), [])
        self.assertEqual(parse_cells(non_int_gold_value), [])
