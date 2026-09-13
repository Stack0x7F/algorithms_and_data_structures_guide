"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.
Return the merged string."""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1, pointer2 = 0, 0 # создаем два указателя, которые будут указывать на текущий символ в каждой строке
        result = '' 
        while pointer1 < len(word1) and pointer2 < len(word2): # пока хотя бы один из указателей не достигнет конца строки, продолжаем цикл
            result += word1[pointer1]
            result += word2[pointer2]
            pointer1,pointer2 = pointer1 + 1, pointer2 + 1   # перемещаем указатели на следующий символ

        result += word1[pointer1:] # добавляем оставшиеся символы из первой строки, если они есть
        result += word2[pointer2:] # добавляем оставшиеся символы из второй строки, если они есть
        
        return result
    
    
"""самый примитивный способ решения задачи, но он работает.
(я не придумал решения лучше, чем это)
Сложность O(n)"""