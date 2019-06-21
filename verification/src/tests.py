"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ((1982, 4, 19), (1982, 4, 22)),
            "answer": 3
        },
        {
            "input": ((2014, 1, 1), (2014, 8, 27)),
            "answer": 238
        },
        {
            "input": ((2014, 8, 27), (2014, 1, 1)),
            "answer": 238
        },

    ],
    "Extra": [
        {
            "input": ((1, 1, 1), (9999, 12, 31)),
            "answer": 3652058
        },
        {
            "input": ((9999, 12, 31), (1, 1, 1)),
            "answer": 3652058
        },
        {
            "input": ((1970, 1, 1), (2000, 1, 1)),
            "answer": 10957
        },
        {
            "input": ((2014, 2, 28), (2014, 2, 28)),
            "answer": 0
        },
        {
            "input": ((2012, 2, 29), (2014, 2, 28)),
            "answer": 730
        },

        {
            "input": ((7015, 1, 11), (8992, 2, 21)),
            "answer": 722126
        },
        {
            "input": ((7410, 4, 9), (9884, 3, 16)),
            "answer": 903587
        },
        {
            "input": ((4139, 10, 30), (4923, 12, 23)),
            "answer": 286404
        },
        {
            "input": ((1622, 10, 4), (3555, 10, 12)),
            "answer": 706021
        },
        {
            "input": ((5871, 8, 23), (6155, 6, 14)),
            "answer": 103659
        },
        {
            "input": ((4632, 11, 18), (8077, 10, 26)),
            "answer": 1258238
        },
        {
            "input": ((696, 5, 7), (9241, 6, 27)),
            "answer": 3121048
        },
        {
            "input": ((6051, 1, 23), (4129, 8, 9)),
            "answer": 701798
        },
    ]
}
