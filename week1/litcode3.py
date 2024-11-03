class Solution:
    def myAtoi(self, s: str) -> int:
        # Константы для пределов 32-битного целого числа
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Удаляем ведущие пробелы
        s = s.lstrip()

        # Если строка пуста после удаления пробелов, возвращаем 0
        if not s:
            return 0

        # Определяем знак
        sign = 1
        index = 0
        if s[0] == "-":
            sign = -1
            index = 1
        elif s[0] == "+":
            index = 1

        # Конвертируем цифры в число
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        # Применяем знак к числу
        num *= sign

        # Проверяем выход за пределы 32-битного целого числа
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        # Возвращаем итоговое число
        return num


# Создаем объект класса Solution
solution = Solution()

# Пример ввода
s = input("Введите строку: ")

# Вызываем метод и выводим результат
print(solution.myAtoi(s))
