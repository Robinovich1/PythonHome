from typing import List, Optional


# Определение узла бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Проверяем, есть ли элементы в inorder
        if inorder:
            # Извлекаем значение корня из postorder и удаляем его
            root_value = postorder.pop()
            # Находим индекс корня в inorder
            root_index = inorder.index(root_value)
            # Создаем узел дерева с найденным значением корня
            root_node = TreeNode(root_value)
            # Рекурсивно строим правое поддерево
            root_node.right = self.buildTree(inorder[root_index + 1 :], postorder)
            # Рекурсивно строим левое поддерево
            root_node.left = self.buildTree(inorder[:root_index], postorder)
            return root_node
