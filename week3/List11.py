from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Устанавливаем указатели на начала и конца массива
        left = 0
        right = len(height) - 1
        max_area = 0

        # Пока указатели не пересекутся
        while left < right:
            # Вычисляем текущую площадь
            current_area = min(height[left], height[right]) * (right - left)
            # Обновляем максимальную площадь, если текущая больше
            max_area = max(max_area, current_area)

            # Двигаем указатель, чтобы попытаться увеличить площадь
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
