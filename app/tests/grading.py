import unittest

from ..algorithm import grading_function


class TestGradingFunction(unittest.TestCase):
    """
    TestCase Class used to test the algorithm.
    ---
    Tests are used here to check that the algorithm written
    is working as it should.

    It's best practise to write these tests first to get a
    kind of 'specification' for how your algorithm should
    work, and you should run these tests before committing
    your code to AWS.

    Read the docs on how to use unittest here:
    https://docs.python.org/3/library/unittest.html

    Use grading_function() to check your algorithm works
    as it should.
    """

    def test_evaluate_as_int(self):
        body = {"answer": "45", "response": "45", "params": {"type": "int"}}

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)
        self.assertEqual(response.get("error", False), False)

    def test_invalid_int(self):
        body = {"answer": "0", "response": "1.0", "params": {"type": "int"}}

        response = grading_function(body)

        self.assertIsNotNone(response.get("error", None))

    def test_evaluate_as_float(self):
        body = {"answer": "4.80", "response": "4.8", "params": {"type": "float"}}

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)
        self.assertEqual(response.get("error", False), False)

    def test_invalid_float(self):
        body = {"answer": "abc", "response": "1", "params": {"type": "int"}}

        response = grading_function(body)

        self.assertIsNotNone(response.get("error", None))

    def test_evaluate_as_string(self):
        body = {
            "answer": "dogs",
            "response": "dogs",
            "params": {"type": "str"},
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)
        self.assertEqual(response.get("error", False), False)

    def test_evaluate_as_string_incorrect(self):
        body = {
            "answer": "1.0",
            "response": "1",
            "params": {"type": "str"},
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), False)

    def test_evaluate_as_dict(self):
        body = {
            "answer": {"a": 1, "b": 2},
            "response": {"b": 2, "a": 1},
            "params": {"type": "dict"},
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)
        self.assertEqual(response.get("error", False), False)


if __name__ == "__main__":
    unittest.main()
