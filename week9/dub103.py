from collections import deque
from typing import List, Optional


# Определение узла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Если дерева нет, возвращаем пустой список

        result = []  # Список для хранения результата
        queue = deque([root])  # Очередь для обхода в ширину
        left_to_right = True  # Флаг для определения направления обхода

        while queue:
            level_size = len(queue)  # Размер текущего уровня
            level_nodes = []  # Список для хранения значений текущего уровня

            # Обрабатываем все узлы текущего уровня
            for _ in range(level_size):
                node = queue.popleft()  # Извлекаем узел из очереди
                level_nodes.append(
                    node.val
                )  # Добавляем значение узла в текущий уровень

                # Добавляем детей узла в очередь для следующего уровня
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Если текущий уровень нечётный, то инвертируем порядок
            if not left_to_right:
                level_nodes.reverse()

            # Добавляем текущий уровень в результат
            result.append(level_nodes)

            # Переключаем направление для следующего уровня
            left_to_right = not left_to_right

        return result
