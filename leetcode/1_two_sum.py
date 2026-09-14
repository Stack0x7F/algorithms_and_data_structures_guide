"""You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 """
 
"приведу 2 решения"

#1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j] 
                
"брут-форс, базовое решение в лоб через сложение каждого элемента с каждым"
#O(n^2)


#2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # создаем словарь для "запоминания" уже пройденных элементов
        for idx, num in enumerate(nums): # проходим по всему листу nums
            complement = target - num # вычисляем недостающее значение для каждого элемента
            if complement in seen: # проверяем, добавлялось ли ранее такое значение в словарь
                return [seen[complement], idx] # если да, то возвращаем его + индекс текущего элемента
                
            seen[num] = idx # если не нашлось нужного числа, записываем текущее в хэш мапу
            
"умное решение через хэш-мапу. не такое очевидное"
#O(n)



