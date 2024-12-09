from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Указатель на левую границу окна
        max_len = 0  # Максимальная длина окна
        zero_count = 0  # Счётчик нулей в окне

        # Проходим по массиву с правым указателем
        for right in range(len(nums)):
            # Если текущий элемент — это 0, увеличиваем счётчик нулей
            if nums[right] == 0:
                zero_count += 1

            # Если количество нулей больше k, сдвигаем левый указатель
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Обновляем максимальную длину окна
            max_len = max(max_len, right - left + 1)

        return max_len
