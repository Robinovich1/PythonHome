from typing import List, Optional


# Определение класса для узла графа
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None  # Если узел пустой, возвращаем None

        # Словарь для хранения клонированных узлов
        cloned_nodes = {}

        # Вспомогательная функция для глубокой копии графа
        def dfs(current_node: Node) -> Node:
            if current_node in cloned_nodes:
                return cloned_nodes[current_node]  # Возвращаем уже клонированный узел

            # Клонируем текущий узел
            cloned_node = Node(current_node.val)
            cloned_nodes[current_node] = cloned_node

            # Клонируем соседей
            for neighbor in current_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))

            return cloned_node

        return dfs(node)  # Запускаем DFS от начального узла
