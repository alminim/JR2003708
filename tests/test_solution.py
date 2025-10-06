import unittest
from src.cell_occupant import Dragon, Princess
from src.main import solve


class TestSolution(unittest.TestCase):
    def test_solution(self):
        successful_journey = [
            Dragon(10, 0),
            Dragon(12, 1),
            Princess(2, 3),
            Dragon(1, 4),
            Princess(2, 5),
        ]
        unssuccessful_journey = [
            Dragon(10, 0),
            Dragon(12, 1),
            Princess(2, 3),
            Dragon(1, 4),
            Princess(3, 5),
        ]

        trivial_success = [Dragon(10, 0), Princess(1, 1)]
        trivial_failure = [Dragon(10, 0), Princess(2, 1)]

        self.assertCountEqual(solve(successful_journey), [Dragon(12, 1), Dragon(1, 4)])
        self.assertCountEqual(solve(trivial_success), [Dragon(10, 0)])
        self.assertEqual(solve(unssuccessful_journey), [])
        self.assertEqual(solve(trivial_failure), [])
