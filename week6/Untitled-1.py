class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        start = max_length = 0

        for end in range(len(s)):
            current_char = s[end]
            if current_char in char_index_map and char_index_map[current_char] >= start:
                start = char_index_map[current_char] + 1
            char_index_map[current_char] = end
            max_length = max(max_length, end - start + 1)

        return max_length
