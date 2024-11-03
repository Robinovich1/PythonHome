from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Если строка пуста, возвращаем пустой список
        if not digits:
            return []

        # Сопоставление цифр с буквами, как на телефонной клавиатуре
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Рекурсивная функция для получения комбинаций
        def backtrack(index, current_combination):
            # Если длина текущей комбинации равна длине digits, добавляем её в результат
            if index == len(digits):
                result.append(current_combination)
                return

            # Получаем буквы, соответствующие текущей цифре
            possible_letters = phone_map[digits[index]]

            # Для каждой буквы добавляем её к текущей комбинации и продолжаем рекурсию
            for letter in possible_letters:
                backtrack(index + 1, current_combination + letter)

        # список результатов
        result = []

        # Запускаем рекурсивную функцию с начальными параметрами
        backtrack(0, "")

        return result


solution = Solution()
s = input("Введите число: ")
print(solution.letterCombinations(s))
