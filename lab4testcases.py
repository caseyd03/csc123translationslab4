import unittest
from index.py import *

class TestLab4(unittest.TestCase):

    def test_counties_with_most_cs(self):
        arr = ['Santa Clara', 'Kern', 'Placer', 'Santa Barbara', 'Orange']
        self.assertEqual(counties_with_most_cs(CALIFORNIA_COUNTIES, PERCENT_SCHOOLS_OFFERING_CS), arr)

    def test_counties_with_least_cs(self):
        arr = ['Colusa', 'Mariposa', 'Modoc', 'San Benito', 'Sierra']
        self.assertEqual(counties_with_least_cs(CALIFORNIA_COUNTIES, PERCENT_SCHOOLS_OFFERING_CS), arr)

    def test_lower_than_avg_cs_counties(self):
        arr = ['Butte', 'Colusa', 'Del Norte', 'El Dorado', 'Fresno', 'Glenn', 'Humboldt', 'Inyo', 'Kings', 'Lake', 'Lassen', 'Madera', 'Mariposa', 'Mendocino', 'Modoc', 'Mono', 'Plumas', 'Sacramento', 'San Benito', 'Sierra', 'Stanislaus', 'Sutter', 'Tehama', 'Trinity', 'Tulare', 'Tuolumne', 'Yuba']
        self.assertEqual(lower_than_avg_cs_counties(CALIFORNIA_COUNTIES, PERCENT_SCHOOLS_OFFERING_CS), arr)

if __name__ == '__main__':
    unittest.main()
