from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Инициализируем левую и правую границы для бинарного поиска
        left, right = 0, len(nums) - 1

        # Начинаем бинарный поиск
        while left <= right:
            mid = (left + right) // 2  # Находим середину

            # Если элемент в середине равен целевому, возвращаем его индекс
            if nums[mid] == target:
                return mid

            # Проверяем, какая из половин отсортирована
            if nums[left] <= nums[mid]:
                # Левая половина отсортирована
                if nums[left] <= target < nums[mid]:
                    # Если целевой элемент находится в левой половине
                    right = mid - 1
                else:
                    # Иначе двигаемся в правую половину
                    left = mid + 1
            else:
                # Правая половина отсортирована
                if nums[mid] < target <= nums[right]:
                    # Если целевой элемент находится в правой половине
                    left = mid + 1
                else:
                    # Иначе двигаемся в левую половину
                    right = mid - 1

        # Если не нашли целевой элемент, возвращаем -1
        return -1
