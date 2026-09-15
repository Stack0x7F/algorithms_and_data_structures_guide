class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.char_counter(s) == self.char_counter(t)


    def char_counter(self, some_string: str) -> dict:
        seen = {}
        for char in some_string:
            if char in seen:
                seen[char] += 1

            else:
                seen[char] = 1
    
        
        return seen
    
# можно решить через сортировку строк, но как будто неправильно юзать такой метод, когда можно просто посчитать количество каждого символа в строке и сравнить их.