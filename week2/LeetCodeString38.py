class Solution:
    def countAndSay(self, n: int) -> str:
        # Базовый случай: первая последовательность — это строка "1"
        current = "1"

        # Генерируем последовательность  от 2 до n
        for h in range(1, n):
            next_seq = ""  # Строка для следующей последовательности
            i = 0  # Индекс для обхода текущей последовательности

            while i < len(current):
                count = 1  # счетчик одинаковых символов

                # Считаем количество одинаковых подряд идущих символов
                while i + 1 < len(current) and current[i] == current[i + 1]:
                    i += 1
                    count += 1

                # Добавляем количество и символ к следующей последовательности
                next_seq += str(count) + current[i]
                i += 1  # Переходим к следующему символу

            # Переходим к следующей последовательности
            current = next_seq

        # Возвращаем  последовательность
        return current


solution = Solution()
n = int(input())
result = solution.countAndSay(n)
print(result)
