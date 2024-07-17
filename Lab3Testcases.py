import unittest
from index import *
from unittest.mock import patch 


class TestLab3(unittest.TestCase):

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

    # Testing Part 1
 
    # def test_counties_with_most_cs(self):
    #     arr = ['Santa Clara', 'Kern', 'Placer', 'Santa Barbara', 'Orange']
    #     self.assertEqual(counties_with_most_cs(CALIFORNIA_COUNTIES, PERCENT_SCHOOLS_OFFERING_CS), arr)

    # def test_counties_with_least_cs(self):
    #     arr = ['Colusa', 'Mariposa', 'Modoc', 'San Benito', 'Sierra']
    #     self.assertEqual(counties_with_least_cs(CALIFORNIA_COUNTIES, PERCENT_SCHOOLS_OFFERING_CS), arr)

    # Testing Part 2
    # def test_question1(self):
    #         self.assertIn("There are 58 counties and 58 proportions.", self.held_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()