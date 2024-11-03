from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Шаг 1: Определяем, нужно ли обнулять первую строку и первый столбец
        zero_first_row = any(matrix[0][j] == 0 for j in range(n))
        zero_first_col = any(matrix[i][0] == 0 for i in range(m))

        # Шаг 2: Используем первую строку и первый столбец для маркировки нулей
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Отмечаем начало строки
                    matrix[0][j] = 0  # Отмечаем начало столбца

        # Шаг 3: Обнуляем ячейки на основе меток в первой строке и первом столбце
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Шаг 4: Обнуляем первую строку и первый столбец, если это необходимо
        if zero_first_row:
            for j in range(n):
                matrix[0][j] = 0

        if zero_first_col:
            for i in range(m):
                matrix[i][0] = 0


# Пример использования:
if __name__ == "__main__":
    sol = Solution()
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix1)
    print(matrix1)

    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix2)
    print(matrix2)
