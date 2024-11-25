from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Словарь для подсчета символов строки s1
        s1_count = Counter(s1)
        # Словарь для подсчета символов текущего окна строки s2
        window_count = Counter()
        # Длина строки s1
        s1_len = len(s1)

        for i in range(len(s2)):
            # Добавляем текущий символ в окно
            window_count[s2[i]] += 1

            # Если окно становится больше длины s1, уменьшаем счетчик символа,
            # который выходит за пределы окна
            if i >= s1_len:
                if window_count[s2[i - s1_len]] == 1:
                    del window_count[s2[i - s1_len]]
                else:
                    window_count[s2[i - s1_len]] -= 1

            # Если счетчики символов совпадают, это означает,
            # что подстрока s2 содержит перестановку s1
            if window_count == s1_count:
                return True

        return False
