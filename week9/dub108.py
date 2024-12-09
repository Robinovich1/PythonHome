from collections import deque
from typing import List, Optional


# Определение узла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Если дерева нет, возвращаем пустой список

        result = []  # Список для хранения результата
        queue = deque([root])  # Очередь для обхода в ширину, начинаем с корня

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

            # Добавляем текущий уровень в результат
            result.append(level_nodes)

        return result
