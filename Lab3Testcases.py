import unittest
from index import *
from unittest.mock import patch 


class TestLab3(unittest.TestCase):

    #Part 2 Test Cases 
    
    @patch('builtins.print')
    def test_print_output(self, question_one):
        with open('index.py') as f:
            exec(f.read()) 

        question_one.assert_any_call("There are 57 counties and 57 proportions.")
    
    @patch('builtins.print')
    def test_print_output(self, question_two):
        with open('index.py') as f:
            exec(f.read()) 

        question_two.assert_any_call("Santa Clara has the highest proportion of schools (0.658228) offering CS courses.")

    @patch('builtins.print')
    def test_print_output(self, question_three):
        with open('index.py') as f:
            exec(f.read()) 

        question_three.assert_any_call("Colusa has the lowest proportion of schools (0.0) offering CS courses.")
        self.assertEqual(question_three.call_count, 3)

if __name__ == '__main__':
    unittest.main()