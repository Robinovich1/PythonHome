from collections import deque
from typing import List, Optional

from week5.hash105 import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        first = second = prev = None  # Указатели для хранения нарушенных узлов
        current = root  # Текущий узел для обхода

        while current:
            # Если у текущего узла нет левого поддерева, посещаем его
            if not current.left:
                # Проверяем, нарушает ли текущий узел свойство BST
                if prev and current.val < prev.val:
                    if not first:
                        first = prev  # Сохраняем первый нарушенный узел
                    second = current  # Сохраняем второй нарушенный узел
                prev = current  # Обновляем предыдущий узел
                current = current.right  # Переходим к правому поддереву
            else:
                # Находим предшественника текущего узла
                pred = current.left
                while pred.right and pred.right != current:
                    pred = (
                        pred.right
                    )  # Ищем правую самую глубокую ветвь в левом поддереве

                # Создаем временную связь от предшественника к текущему узлу
                if not pred.right:
                    pred.right = current
                    current = current.left  # Переходим в левое поддерево
                else:
                    # Убираем временную связь, посещаем текущий узел
                    if prev and current.val < prev.val:
                        if not first:
                            first = prev  # Сохраняем первый нарушенный узел
                        second = current  # Сохраняем второй нарушенный узел
                    prev = current  # Обновляем предыдущий узел
                    pred.right = None  # Убираем временную связь
                    current = current.right  # Переходим в правое поддерево

        # После обхода дерева меняем местами значения двух нарушенных узлов
        if first and second:
            first.val, second.val = second.val, first.val
