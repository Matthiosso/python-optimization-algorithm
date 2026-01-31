import unittest

from solver_there_is_no_spoon import solve_there_is_no_spoon_problem

class TestSolveThereIsNoSpoonProblem(unittest.TestCase):

    def test_example_1(self):
        input_matrix = [
            '00',
            '0.'
        ]
        result = solve_there_is_no_spoon_problem(input_matrix)
        expected = [
            '0 0 1 0 0 1',
            '1 0 -1 -1 -1 -1',
            '0 1 -1 -1 -1 -1'
        ]
        self.assertEqual(result, expected)

    def test_example_horizontal(self):
        input_matrix = [
            '0.0.0'
        ]
        result = solve_there_is_no_spoon_problem(input_matrix)
        expected = [
            '0 0 2 0 -1 -1',
            '2 0 4 0 -1 -1',
            '4 0 -1 -1 -1 -1',
        ]
        self.assertEqual(result, expected)

    
    def test_example_vertical(self):
        input_matrix = [
            '0',
            '.',
            '0',
            '.',
            '0'
        ]
        result = solve_there_is_no_spoon_problem(input_matrix)
        expected = [
            '0 0 -1 -1 0 2',
            '0 2 -1 -1 0 4',
            '0 4 -1 -1 -1 -1',
        ]
        self.assertEqual(result, expected)

    def test_square(self):
        input_matrix = [
            '0.0',
            '...',
            '0.0'
        ]
        result = solve_there_is_no_spoon_problem(input_matrix)
        expected = [
            '0 0 2 0 0 2',
            '2 0 -1 -1 2 2',
            '0 2 2 2 -1 -1',
            '2 2 -1 -1 -1 -1'
        ]
        self.assertEqual(result, expected)