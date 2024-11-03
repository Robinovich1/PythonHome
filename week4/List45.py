from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Инициализация переменных для отслеживания прыжков
        jumps = 0
        current_end = 0
        farthest = 0

        # Проходим по каждому элементу массива, кроме последнего
        for i in range(len(nums) - 1):
            # Обновляем самую дальнюю позицию, до которой можно дойти
            farthest = max(farthest, i + nums[i])

            # Если текущий индекс достиг конца текущего прыжка
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
