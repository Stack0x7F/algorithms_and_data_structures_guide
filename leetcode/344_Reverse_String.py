"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""


# базовый способ решения через два указателя, которые двигаются навстречу друг другу и сравнивают символы, при этом игнорируя лишние символы и приводя к нижнему регистру

from ast import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
            