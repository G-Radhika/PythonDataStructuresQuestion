"""
Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.

@param {string} s input string
@return {bool} if string is palindrome or not
"""

def isPalindrome(s):
    if not s:
        return False
    # reverse compare
    return s == s[::-1]

# @param {string} s input string
# @return {string} the longest palindromic substring


def question2(s):
    if not s:
        return ""

    n = len(s)
    longest, left, right = 0, 0, 0
    for i in xrange(0, n):
        for j in xrange(i + 1, n + 1):
                   substr = s[i:j]
                   if isPalindrome(substr) and len(substr) > longest:
                       longest = len(substr)
                       left, right = i, j
    # construct longest substr
    result = s[left:right]
    return result
#
# Test Cases

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():  
  print 'question 2'
  # Each line calls donuts, compares its result to the expected for that call.
  test(question2("AABCCBAC"), 'ABCCBA')
  test(question2("ABCDDCBA"), 'ABCDDCBA')
  test(question2("ABACCARA"), 'ACCA')
  test(question2("ABATC"), 'ABA')