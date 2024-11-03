from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Отсортируем массив, чтобы легче было работать с двумя указателями
        nums.sort()
        result = []

        # Проходим по массиву, фиксируя первый элемент тройки
        for i in range(len(nums) - 2):
            # Пропускаем одинаковые элементы, чтобы избежать дубликатов
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Инициализируем два указателя
            left, right = i + 1, len(nums) - 1

            # Используем два указателя для поиска второй и третьей тройки
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Если сумма равна 0, добавляем тройку в результат
                    result.append([nums[i], nums[left], nums[right]])

                    # Пропускаем одинаковые значения, чтобы избежать дубликатов
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Сдвигаем оба указателя
                    left += 1
                    right -= 1
                elif total < 0:
                    # Если сумма меньше 0, двигаем указатель `left` вправо
                    left += 1
                else:
                    # Если сумма больше 0, двигаем указатель `right` влево
                    right -= 1

        return result
