class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Словарь для подсчета частот символов в текущем окне
        char_count = {}
        left = 0
        max_freq = 0  # Максимальная частота символа в текущем окне
        max_length = 0  # Максимальная длина подстроки

        for right in range(len(s)):
            # Добавляем текущий символ в словарь
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Обновляем максимальную частоту символа в текущем окне
            max_freq = max(max_freq, char_count[s[right]])

            # Проверяем, можно ли преобразовать текущее окно
            if (right - left + 1) - max_freq > k:
                # Уменьшаем окно, удаляя символ слева
                char_count[s[left]] -= 1
                left += 1

            # Обновляем максимальную длину
            max_length = max(max_length, right - left + 1)

        return max_length
