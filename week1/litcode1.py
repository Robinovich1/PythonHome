class Solution:
    def lengthOfLongestSubstring(self, s1: str) -> int:
        char_index = {}  # Словарь для хранения индексов символов
        left = 0  # Левый указатель
        max_length = 0  # Максимальная длина подстроки
        s = ""
        s = s1

        # Проходим по каждому символу строки
        for right in range(len(s)):
            # Если символ уже встречался и его индекс больше или равен left,
            # передвигаем левый указатель вправо
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            # Обновляем индекс текущего символа
            char_index[s[right]] = right

            # Вычисляем длину текущей подстроки и обновляем максимальную длину
            max_length = max(max_length, right - left + 1)

            # print(max_length)

        return max_length


solution = Solution()
st = input()
# solution.lengthOfLongestSubstring(st)

# Вызываем метод lengthOfLongestSubstring и передаем строку st
print(solution.lengthOfLongestSubstring(st))
