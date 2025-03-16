import pytest
from solution import Solution  # Assuming the function is defined in solution.py

@pytest.fixture
def solution():
    return Solution()

# Define test cases in a structured format
testcases = [
    # (s, p, expected_res)
    ("", "", True),
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".", True),
    ("a", "..", False),  # This should be False, as ".." needs two characters
    ("aab", "c*a*b", True),
    ("aaa", "ab*a*c*a", True)
]

@pytest.mark.parametrize("s, p, expected", testcases)
def test_regex_matching(solution,s, p, expected):
    assert solution.isMatch(s, p) == expected

# Handling expected failure
@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch("mississippi", "mis*is*p*.") == True