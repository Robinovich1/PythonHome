class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Возвращаем подстроку, которая является палиндромом
            return s[left + 1 : right]

        # Если строка пустая или состоит из одного символа
        if len(s) < 2:
            return s

        longest_palindrome = ""

        for i in range(len(s)):
            # Для палиндромов с нечетной длиной
            odd_palindrome = expandAroundCenter(i, i)
            # Для палиндромов с четной длиной
            even_palindrome = expandAroundCenter(i, i + 1)

            # Обновляем максимальный палиндром
            longest_palindrome = max(
                longest_palindrome, odd_palindrome, even_palindrome, key=len
            )

        return longest_palindrome


solution = Solution()
st = input()
print(solution.longestPalindrome(st))
