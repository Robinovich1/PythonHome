from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Словарь для подсчета символов в строке p
        p_count = Counter(p)
        # Словарь для подсчета символов в текущем окне строки s
        s_count = Counter()
        # Длина строки p
        p_len = len(p)
        # Результат — список индексов
        result = []

        for i in range(len(s)):
            # Добавляем текущий символ в окно
            s_count[s[i]] += 1

            # Если окно больше размера p, удаляем символ, выходящий из окна
            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                else:
                    s_count[s[i - p_len]] -= 1

            # Если счетчики совпадают, добавляем индекс начала окна
            if s_count == p_count:
                result.append(i - p_len + 1)

        return result
