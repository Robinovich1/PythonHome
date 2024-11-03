from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # Вспомогательная функция для поиска комбинаций
        def backtrack(remaining: int, combination: List[int], start: int):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Добавляем кандидата в текущую комбинацию
                combination.append(candidates[i])
                # Рекурсивно вызываем backtrack, с возможностью выбора текущего числа еще раз
                backtrack(remaining - candidates[i], combination, i)
                # Убираем последнее число из комбинации для исследования других путей
                combination.pop()

        backtrack(target, [], 0)
        return result
