from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Словарь для хранения количества встреченных префиксных сумм
        prefix_sum_count = defaultdict(int)
        # Начальная префиксная сумма равна 0, так как префиксная сумма до первого элемента - это 0
        prefix_sum_count[0] = 1

        current_sum = 0  # Текущая префиксная сумма
        result = 0  # Количество подмассивов, сумма которых равна goal

        # Проходим по всем элементам массива
        for num in nums:
            # Обновляем текущую префиксную сумму
            current_sum += num

            # Если мы можем найти подмассив, который имеет сумму goal, то увеличиваем результат
            # Нужно, чтобы current_sum - goal была в словаре (это будет префиксная сумма до некоторого индекса)
            result += prefix_sum_count[current_sum - goal]

            # Добавляем текущую префиксную сумму в словарь
            prefix_sum_count[current_sum] += 1

        return result
