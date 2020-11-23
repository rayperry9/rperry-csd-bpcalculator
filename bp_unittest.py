#!/usr/local/bin/python3

import unittest
from unittest.mock import patch
from bp_calculator import get_input, get_results

class TestBpCalc (unittest.TestCase):


    # def test_main(capsys):
    #     main()
    #     captured = capsys.readouterr()
    #     assert captured.out == 'Welcome to BP calculator'


# Testing get_input functionality
    @patch('builtins.input')
    def test_invalidsys(self, input):
        get_input('a', 'b')
        self.assertRaisesRegex(ValueError, "Please only enter numbers")

    @patch('builtins.input')
    def test_invalddias(self, input):
        get_input('100', '?')
        self.assertRaisesRegex(ValueError, "Please only enter numbers")

    @patch('builtins.input')
    def test_invalidrangesys(self, input):
        get_input('8000', '80')
        self.assertRaisesRegex(ValueError, "Invalid Systolic Value, please re-enter value.")

    @patch('builtins.input')
    def test_invalidrangedias(self, input):
        get_input('100', '8000')
        self.assertRaisesRegex(ValueError, "Invalid Diastolic Value, please re-enter value.")

    @patch('builtins.input')
    def test_valid(self, input):
        get_input('80', '50')


# Testing get_results functionality
    def test_lowblood(self):
        result = get_results(85, 55)
        self.assertEqual(result, "Low blood pressure")

    def test_idealblood(self):
        result = get_results(100, 70)
        self.assertEqual(result, "Ideal blood pressure")

    def test_preblood(self):
        result = get_results(130, 55)
        self.assertEqual(result, "Pre-high blood pressure")

    def test_highlood(self):
        result = get_results(150, 70)
        self.assertEqual(result, "High blood pressure")

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))