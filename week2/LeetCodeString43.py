class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Если одно из чисел 0, результат будет 0
        if num1 == "0" or num2 == "0":
            return "0"

        # Массив для хранения результатов умножения на каждом шаге
        result = [0] * (len(num1) + len(num2))

        # Проходим по каждой цифре числа num1 и умножаем на num2
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Переводим символы в числа
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))

                # Индексы для текущей позиции результата
                p1 = i + j
                p2 = i + j + 1

                # Добавляем текущее произведение в результат
                sum = mul + result[p2]

                # Записываем остаток и перенос
                result[p2] = sum % 10
                result[p1] += sum // 10

        # Преобразуем результат в строку
        result_str = "".join(map(str, result)).lstrip("0")

        # Возвращаем результат
        return result_str if result_str else "0"


solution = Solution()
n = input()
m = input()
result = solution.multiply(n, m)
print(result)
