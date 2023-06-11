"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[2, 2]],
            "answer": 2,
        },
        {
            "input": [[4, 3, 2, 1]],
            "answer": 0,
        },
        {
            "input": [[5, 3, 4, 2]],
            "answer": 7,
        },
        {
            "input": [[8, 8, 8, 8, 8, 9, 9]],
            "answer": 1895245,
        },
    ],
    "Extra": [
        {
            "input": [[4, 4]],
            "answer": 5,
        },
        {
            "input": [[6, 8, 6, 8, 6, 8]],
            "answer": 6728,
        },
        {
            "input": [[12, 12, 11, 11, 11, 11, 11, 11]],
            "answer": 13571985717,
        },
        {
            "input": [[6]*23],
            "answer": 5791672851807481,
        }
    ]
}
