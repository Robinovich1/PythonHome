from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Сортируем массив для удобства использования двух указателей
        nums.sort()

        closest_sum = float("inf")

        # Проходим по каждому элементу массива (за исключением последних двух)
        for i in range(len(nums) - 2):
            # Используем метод двух указателей
            left, right = i + 1, len(nums) - 1

            # Пока левый указатель находится левее правого
            while left < right:
                # Суммируем текущие три числа
                current_sum = nums[i] + nums[left] + nums[right]

                # Если сумма точно равна целевому значению, возвращаем её сразу
                if current_sum == target:
                    return current_sum

                # Если текущая сумма ближе к целевому значению, чем предыдущая, обновляем ближайшую сумму
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Если текущая сумма меньше целевой, сдвигаем левый указатель вправо
                if current_sum < target:
                    left += 1
                # Если текущая сумма больше целевой, сдвигаем правый указатель влево
                else:
                    right -= 1

        # Возвращаем ближайшую найденную сумму
        return closest_sum
