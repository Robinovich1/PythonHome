from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Сортируем массив для удобства работы с указателями
        nums.sort()
        n = len(nums)
        result = []

        # Фиксируем первые два элемента через вложенные циклы
        for i in range(n - 3):
            # Пропускаем одинаковые значения для первого элемента, чтобы избежать дубликатов
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # Пропускаем одинаковые значения для второго элемента
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Используем два указателя для поиска оставшихся двух чисел
                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        # Если сумма равна target, добавляем четверку в результат
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Пропускаем одинаковые значения для указателя left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Пропускаем одинаковые значения для указателя right
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Сдвигаем оба указателя
                        left += 1
                        right -= 1
                    elif total < target:
                        # Если сумма меньше target, двигаем указатель left вправо
                        left += 1
                    else:
                        # Если сумма больше target, двигаем указатель right влево
                        right -= 1

        return result
