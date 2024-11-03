from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Результирующий список
        result = []
        # Сортируем кандидатов для удобства обработки дубликатов
        candidates.sort()

        # Вспомогательная функция для поиска комбинаций
        def backtrack(remaining: int, combination: List[int], start: int):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Пропускаем дубликаты
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Добавляем кандидата в текущую комбинацию
                combination.append(candidates[i])
                # Рекурсивно вызываем backtrack с уменьшенной суммой и следующим индексом
                backtrack(remaining - candidates[i], combination, i + 1)
                # Убираем последнее число для исследования других комбинаций
                combination.pop()

        # Запуск backtracking с начальной суммой target
        backtrack(target, [], 0)
        return result
