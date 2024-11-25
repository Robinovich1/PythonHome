from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  # Если k <= 1, ни один подмассив не будет удовлетворять условию
            return 0

        product = 1
        left = 0
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            # Сдвигаем левый указатель, пока произведение >= k
            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            # Все подмассивы от left до right включительно подходят
            count += right - left + 1

        return count
