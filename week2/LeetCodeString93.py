class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def is_valid(segment: str) -> bool:
            # Проверка на допустимость сегмента
            if len(segment) > 1 and segment[0] == "0":
                return False
            return 0 <= int(segment) <= 255  # Число должно быть в пределах от 0 до 255

        def backtrack(start: int, parts: list[str]):
            # Если нашли 4 части и использовали все символы строки, сохраняем результат
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            # Генерация следующих частей
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start : start + length]
                    if is_valid(segment):
                        backtrack(start + length, parts + [segment])

        result = []
        backtrack(0, [])
        return result


solution = Solution()
n = input()
result = solution.restoreIpAddresses(n)
print(result)
