#!/usr/bin/env python3

import unittest
from unittest import mock

from fibonacci import *

class FibonacciTest(unittest.TestCase):
    #handleMenuInput: given integer is returned, empty input returns 10 when
    #the flag enabling empty inputs is set to true
    @mock.patch('fibonacci.input', create=True)
    def test_handleMenuInputCorrect(self, mock_input):
        mock_input.side_effect = [5, ""]
        self.assertEqual(handleMenuInput("", False), 5)
        self.assertEqual(handleMenuInput("", True), 10)

    #handleMenuInput: test for wrong parameter datatype raising an error
    @mock.patch('fibonacci.input', create=True)
    def test_handleMenuInputBadDatatype(self, mock_input):
        mock_input.side_effect = ["abc", [], "fg7gf7gf5"]
        for i in mock_input.side_effect:
            with self.assertRaises(ValueError):
                handleMenuInput("Starting number for the Fibonacci series? ", False)

    #handleMenuInput: ValueError should be raised when input is empty
    #but the flag enabling empty inputs is set to false
    @mock.patch('fibonacci.input', create=True)
    def test_handleMenuInputEmptyInputWhenNotAllowed(self, mock_input):
        mock_input.side_effect = [""]
        with self.assertRaises(ValueError):
            handleMenuInput("Starting number for the Fibonacci series? ", False)

    #getFibonacciSeries: check for correct series for the given parameters
    def test_getFibonacciSeriesCorrectResult(self):
        fibo1 = [987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]
        self.assertEqual(getFibonacciSeries(747, 10), fibo1)
        fibo2 = [6765, 10946, 17711, 28657, 46368]
        self.assertEqual(getFibonacciSeries(6488, 5), fibo2)

    #fibonacci: test for correct output in the specified file
    @mock.patch('fibonacci.input', create=True)
    def test_fibonacciFileOutput(self, mock_input):
        mock_input.side_effect = [-1, 9]
        main()

        file = open("fibonacciSeries.txt")
        output = file.read()
        file.close()

        expectedOutput = "0, 1, 1, 2, 3, 5, 8, 13, 21"

        self.assertEqual(output, expectedOutput)

if __name__ == "__main__":
    unittest.main()
