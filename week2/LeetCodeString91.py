class Solution:
    def numDecodings(self, s: str) -> int:
        # Если строка пуста или начинается с 0, то декодирование невозможно
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        # Базовые случаи - пустая строка имеет один способ декодирования (ничего не делать)
        dp[0] = 1
        # Строка длиной 1 имеет один способ, если не начинается с 0
        dp[1] = 1 if s[0] != "0" else 0

        # Заполняем массив
        for i in range(2, n + 1):
            # Односимвольное декодирование
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # Двухсимвольное декодирование ,если число от 10 до 26
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]


solution = Solution()
n = input()
result = solution.numDecodings(n)
print(result)
