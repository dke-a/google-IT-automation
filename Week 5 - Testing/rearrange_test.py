from rearrange import rearrange_name
import unittest 

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)
        # sample of an edge case
        # Edge Cases are inputs to code that produce
        #   unexpected results, and are found at
        #   extreme ends of the ranges of input that
        #   we typically work with.

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase),expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase),expected)
        #raises assertion error since empty string is returned


unittest.main()