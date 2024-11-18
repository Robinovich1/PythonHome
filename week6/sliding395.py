from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        char_count = Counter(s)

        for char in char_count:
            if char_count[char] < k:

                return max(
                    self.longestSubstring(sub_str, k) for sub_str in s.split(char)
                )

        return len(s)
