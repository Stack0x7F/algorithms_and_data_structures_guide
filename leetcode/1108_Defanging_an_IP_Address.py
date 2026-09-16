class Solution:
    def defangIPaddr(self, address: str) -> str:

        modyfied_string = []
        for char in range(len(address)):
            if address[char] != '.':
                modyfied_string.append(address[char])
            else:
                modyfied_string.append('[.]')

        result = ''
        for element in modyfied_string:
            result += element

        return result
    
# решение без replace 