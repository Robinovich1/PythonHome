from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Проверяем строки, столбцы и блоки 3x3
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                # Пропускаем пустые клетки
                if num == ".":
                    continue

                # Проверяем строку
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # Проверяем столбец
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # Проверяем блок 3x3
                box_index = (i // 3) * 3 + j // 3
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

        return True
