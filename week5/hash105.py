from typing import List, Optional


# Определение узла бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # Словарь для быстрого поиска индексов значений в inorder
        inorder_index = {value: index for index, value in enumerate(inorder)}

        # Вложенная функция для построения дерева
        def construct_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Корень — последний элемент в postorder
            root_value = postorder.pop()  # Удаляем последний элемент
            root = TreeNode(root_value)

            # Индекс корня в inorder
            index = inorder_index[root_value]

            # Рекурсивно строим правое и левое поддеревья
            root.right = construct_tree(index + 1, right)
            root.left = construct_tree(left, index - 1)

            return root

        return construct_tree(0, len(inorder) - 1)


# Пример использования
if __name__ == "__main__":
    sol = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    tree = sol.buildTree(inorder, postorder)

    # Функция для проверки структуры дерева (inorder обход)
    def inorder_traversal(node):
        return (
            inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
            if node
            else []
        )

    print(inorder_traversal(tree))  # Должно вернуть [9, 3, 15, 20, 7]
