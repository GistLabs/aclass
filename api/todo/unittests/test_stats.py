import json
from unittest import TestCase
from todo.stats import DataStats


test_data = [
    {
        "id": 1,
        "name": "Laith",
        "surname": "Simmons",
        "age": 68,
        "salary": "$27888"
    },
    {
        "id": 2,
        "name": "Mikayla",
        "surname": "Henry",
        "age": 49,
        "salary": "$67137"
    },
    {
        "id": 3,
        "name": "Garth",
        "surname": "Fields",
        "age": 70,
        "salary": "$70472"
    }
]


class TestDataData(TestCase):

    def test_json(self):

        ds = DataStats()

        expected_output = json.dumps(
            {
                'avg_age': 62,
                'avg_salary': 55165,
                'avg_yearly_increase': 837,
                'max_salary': [{
                    "id": 3,
                    "name": "Garth",
                    "surname": "Fields",
                    "age": 70,
                    "salary": "$70472"
                }],
                'min_salary': [{
                    "id": 1,
                    "name": "Laith",
                    "surname": "Simmons",
                    "age": 68,
                    "salary": "$27888"
                }]
            }
        )

        self.assertEqual(expected_output, ds.stats(test_data, 20, 20000))