from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Бинарный поиск для нахождения точки начала окна
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # Сравниваем расстояния от x до mid и mid + k
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        # Возвращаем окно длиной k начиная с left
        return arr[left : left + k]
