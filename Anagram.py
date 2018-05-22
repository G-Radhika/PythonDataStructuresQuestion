"""
Question 1
Given two strings s and t, determine whether some anagram of t is a
substring of s. For example: if s = "udacity" and t = "ad",
then the function returns True. Your function definition should
look like: question1(s, t) and return a boolean True or False.
TO DO: Create a “window” with the same size as t.
Move this window through s.
At each iteration check that the character frequency of that window
equals the character frequency of t. If you do this cleverly it can
be done in O(1) time.

Runtime: O(s)
Space: O(1)
"""

import itertools


def question1(s, t):
    # 1. check if t is not empty
    if len(t) == 0:
        return False
    elif len(t) == 1:  # t has only one letter, so cannot make any combinations
        return False
    elif len(t) > len(s):
        return False
    else:
        return compare(s, t)


def compare(s, t):
    # Make a set of every permutation of s and t
    t_list = list(map("".join, itertools.permutations(t)))
    t_set = set(t_list)
    s_list = list(map("".join, itertools.permutations(s, len(t))))
    s_set = set(s_list)
    for t in t_set:
        if t in s_set:
            return True
        else:
            return False


# Simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test_anagram(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
