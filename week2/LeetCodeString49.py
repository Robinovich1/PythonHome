from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Создаем для хранения анаграмм
        anagrams = defaultdict(list)

        # Проходим по каждой строке в массиве
        for word in strs:
            # Сортируем буквы в слове
            sorted_word = "".join(sorted(word))
            # Добавляем исходное слово в список
            anagrams[sorted_word].append(word)

        # Возвращаем все сгруппированные анаграммы
        return list(anagrams.values())


solution = Solution()

n = int(input())
s = [""] * n
for i in range(n):
    s[i] = input()
result = solution.groupAnagrams(s)
print(result)
