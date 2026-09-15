"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""


#1 способ решения через очистку строки от лишних символов и приведение к нижнему регистру, а затем проверка на палиндромность через срезы

class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_string = []
        for char in s:
            if char.isalnum():
                mod_string.append(char.lower())


        return mod_string == mod_string[::-1]
    


#2 решение через два указателя, которые двигаются навстречу друг другу, при этом игнорируя лишние символы и приводя к нижнему регистру, получше по памяти и в целом прикольнее

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
            