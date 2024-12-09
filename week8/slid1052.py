from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # Шаг 1: Рассчитаем количество удовлетворённых клиентов без использования секретной техники
        total_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]

        # Шаг 2: Используем скользящее окно для нахождения максимального числа клиентов,
        # которых можно удовлетворить, если хозяин не серый в период времени `minutes`.
        max_additional_satisfied = 0
        current_additional_satisfied = 0

        # Шаг 3: Инициализация скользящего окна
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]

        # Шаг 4: Двигаем окно по массиву
        max_additional_satisfied = current_additional_satisfied
        for i in range(minutes, len(customers)):
            # Убираем элемент, который выходит из окна
            if grumpy[i - minutes] == 1:
                current_additional_satisfied -= customers[i - minutes]
            # Добавляем новый элемент, который входит в окно
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]

            # Обновляем максимальное количество дополнительных удовлетворённых клиентов
            max_additional_satisfied = max(
                max_additional_satisfied, current_additional_satisfied
            )

        # Шаг 5: Возвращаем итоговое количество удовлетворённых клиентов
        return total_satisfied + max_additional_satisfied
