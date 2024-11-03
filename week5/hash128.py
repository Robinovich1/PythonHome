from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Преобразуем список в множество для быстрого поиска
        longest_streak = (
            0  # Переменная для хранения длины самой длинной последовательности
        )

        for num in num_set:  # Проходим по каждому уникальному числу
            # Проверяем, является ли текущее число началом последовательности
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1  # Длина текущей последовательности

                # Увеличиваем длину последовательности, пока есть последовательные числа
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Обновляем максимальную длину последовательности, если текущая длиннее
                longest_streak = max(longest_streak, current_streak)

        return longest_streak  # Возвращаем длину самой длинной последовательности
