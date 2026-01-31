import unittest

from solver_packets_agents import solve_packets_per_agent_problem

class TestSolvePacketsPerAgentProblem(unittest.TestCase):

    def test_example_1(self):
        result = solve_packets_per_agent_problem([7, 10, 4], 4)
        self.assertEqual(result, 4)
    
    def test_example_2(self):
        result = solve_packets_per_agent_problem([3, 1], 10)
        self.assertEqual(result, 0)
    
    def test_example_3(self):
        result = solve_packets_per_agent_problem([7, 2], 4)
        self.assertEqual(result, 2)
    
    def test_two_agents(self):
        result = solve_packets_per_agent_problem([5, 10, 15], 2)
        self.assertEqual(result, 10)
    
    def test_excess_agents(self):
        result = solve_packets_per_agent_problem([3, 1], 10)
        self.assertEqual(result, 0)
    
    def test_packets_equals_agents(self):
        result = solve_packets_per_agent_problem([3, 1, 2], 6)
        self.assertEqual(result, 1)
    
    def test_zero_agent(self):
        result = solve_packets_per_agent_problem([5, 10, 15], 0)
        self.assertEqual(result, 0)
    
    def test_zero_packet_empty_list(self):
        result = solve_packets_per_agent_problem([], 3)
        self.assertEqual(result, 0)
    
    def test_zero_packet_zero_value(self):
        result = solve_packets_per_agent_problem([0], 3)
        self.assertEqual(result, 0)
    
    def test_one_agent(self):
        result = solve_packets_per_agent_problem([5, 10, 15], 1)
        self.assertEqual(result, 15)
    
    def test_single_packet(self):
        result = solve_packets_per_agent_problem([10], 5)
        self.assertEqual(result, 2)
    
    def test_more_packets_than_agents_easy(self):
        result = solve_packets_per_agent_problem([7, 10, 4, 8, 2, 5], 5)
        self.assertEqual(result, 5)
    
    def test_more_packets_than_agents_hard(self):
        result = solve_packets_per_agent_problem([7, 9, 4, 8, 2, 5], 5)
        self.assertEqual(result, 4)
    
    def test_one_big_packet_easy(self):
        result = solve_packets_per_agent_problem([7, 500, 4, 8, 2, 5], 5)
        self.assertEqual(result, 100)
    
    def test_one_big_packet_hard(self):
        result = solve_packets_per_agent_problem([7, 500, 101, 8, 2, 5], 5)
        self.assertEqual(result, 101)

    def test_one_big_packet_harder(self):
        result = solve_packets_per_agent_problem([7, 500, 200, 8, 2, 5], 5)
        self.assertEqual(result, 125)

    def test_one_big_packet_hardest(self):
        result = solve_packets_per_agent_problem([7, 500, 250, 200, 2, 5], 5)
        self.assertEqual(result, 166)
    
    def test_large_numbers(self):
        result = solve_packets_per_agent_problem([1000000, 2000000, 3000000], 3)
        self.assertEqual(result, 1500000)

    def test_huge_numbers(self):
        result = solve_packets_per_agent_problem([10000001, 10000001, 30000000], 3)
        self.assertEqual(result, 10000001)
    
    def test_all_packets_same_size(self):
        result = solve_packets_per_agent_problem([5, 5, 5, 5], 4)
        self.assertEqual(result, 5)
    
    def test_uneven_distribution(self):
        result = solve_packets_per_agent_problem([15, 10, 5], 5)
        self.assertEqual(result, 5)
    
    def test_prime_numbers(self):
        result = solve_packets_per_agent_problem([17, 13, 11], 6)
        self.assertEqual(result, 5)

    def test_prime_numbers_bis(self):
        result = solve_packets_per_agent_problem([17, 13, 11], 5)
        self.assertEqual(result, 6)
    
    def test_single_packet_single_agent(self):
        result = solve_packets_per_agent_problem([10], 1)
        self.assertEqual(result, 10)
    
    def test_equal_split(self):
        result = solve_packets_per_agent_problem([5, 5, 5], 15)
        self.assertEqual(result, 1)
    
    def test_four_units_two_agents(self):
        result = solve_packets_per_agent_problem([1, 1, 1, 1], 2)
        self.assertEqual(result, 1)
    
    def test_split_equal_packets(self):
        result = solve_packets_per_agent_problem([6, 6, 6], 6)
        self.assertEqual(result, 3)
    
    def test_various_sizes(self):
        result = solve_packets_per_agent_problem([20, 1, 1], 3)
        self.assertEqual(result, 6)
    
    def test_mixed_sizes(self):
        result = solve_packets_per_agent_problem([8, 7, 6, 5], 4)
        self.assertEqual(result, 5)
    
    def test_hundred_split(self):
        result = solve_packets_per_agent_problem([100], 10)
        self.assertEqual(result, 10)
    
    def test_fifty_fifty(self):
        result = solve_packets_per_agent_problem([50, 50], 5)
        self.assertEqual(result, 16)
    
    def test_sequential_packets(self):
        result = solve_packets_per_agent_problem([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 3)
    
    def test_many_small_packets(self):
        result = solve_packets_per_agent_problem([2, 2, 2, 2, 2], 5)
        self.assertEqual(result, 2)
    
    def test_exact_division(self):
        result = solve_packets_per_agent_problem([12], 4)
        self.assertEqual(result, 3)
    
    def test_nine_packets_nine_agents(self):
        result = solve_packets_per_agent_problem([9, 9, 9], 9)
        self.assertEqual(result, 3)
    
    def test_uneven_split(self):
        result = solve_packets_per_agent_problem([11, 7, 3], 5)
        self.assertEqual(result, 3)
    
    def test_mixed_uneven(self):
        result = solve_packets_per_agent_problem([13, 8, 4], 4)
        self.assertEqual(result, 4)
    
    def test_prime_split(self):
        result = solve_packets_per_agent_problem([23], 7)
        self.assertEqual(result, 3)
    
    def test_excess_agents_2(self):
        result = solve_packets_per_agent_problem([10, 5], 20)
        self.assertEqual(result, 0)
    
    def test_excess_agents_3(self):
        result = solve_packets_per_agent_problem([8], 10)
        self.assertEqual(result, 0)
    
    def test_six_units_three_agents(self):
        result = solve_packets_per_agent_problem([1, 1, 1, 1, 1, 1], 3)
        self.assertEqual(result, 1)
    
    def test_minimum_case(self):
        result = solve_packets_per_agent_problem([1], 1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()