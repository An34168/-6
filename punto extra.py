class Machine:
    def __init__(self, productivity, cost, average_part_price):
        """
        Инициализация объекта станка.
        :param productivity: Производительность (изделий в час)
        :param cost: Стоимость станка
        :param average_part_price: Средняя цена детали
        """
        self.productivity = productivity
        self.cost = cost
        self.average_part_price = average_part_price

    def parts_for_breakeven(self):
        """
        Метод для расчёта количества деталей, необходимых для окупаемости станка.
        :return: Количество деталей
        """
        return self.cost / self.average_part_price

    def __add__(self, other):
        """
        Перегрузка оператора сложения.
        Складывает характеристики двух станков, возвращая новый объект Machine.
        """
        if isinstance(other, Machine):
            return Machine(
                productivity=self.productivity + other.productivity,
                cost=self.cost + other.cost,
                average_part_price=(self.average_part_price + other.average_part_price) / 2
            )
        raise ValueError("Сложение возможно только между объектами класса Machine")

    def __str__(self):
        return f"Machine(productivity={self.productivity}, cost={self.cost}, average_part_price={self.average_part_price})"


class MillingMachine(Machine):
    def __init__(self, productivity, cost, average_part_price, milling_precision):
        """
        Инициализация объекта фрезерного станка.
        :param milling_precision: Точность обработки в микрометрах
        """
        super().__init__(productivity, cost, average_part_price)
        self.milling_precision = milling_precision

    def payback_time(self, fixed_part_price):
        """
        Метод для расчёта времени окупаемости станка при фиксированной цене детали.
        :param fixed_part_price: Фиксированная цена детали
        :return: Время окупаемости (в часах)
        """
        total_parts = self.cost / fixed_part_price
        return total_parts / self.productivity

    def __add__(self, other):
        """
        Перегрузка оператора сложения.
        Возвращает новый объект MillingMachine с объединёнными характеристиками.
        """
        if isinstance(other, MillingMachine):
            combined_machine = super().__add__(other)
            return MillingMachine(
                combined_machine.productivity,
                combined_machine.cost,
                combined_machine.average_part_price,
                (self.milling_precision + other.milling_precision) / 2
            )
        return super().__add__(other)

    def __str__(self):
        return (f"MillingMachine(productivity={self.productivity}, cost={self.cost}, "
                f"average_part_price={self.average_part_price}, milling_precision={self.milling_precision})")


class CNC_Machine(Machine):
    def __init__(self, productivity, cost, average_part_price, automation_level):
        """
        Инициализация объекта станка с ЧПУ.
        :param automation_level: Уровень автоматизации (0-100%)
        """
        super().__init__(productivity, cost, average_part_price)
        self.automation_level = automation_level

    def payback_time(self, fixed_part_price):
        """
        Метод для расчёта времени окупаемости станка при фиксированной цене детали.
        :param fixed_part_price: Фиксированная цена детали
        :return: Время окупаемости (в часах)
        """
        total_parts = self.cost / fixed_part_price
        return total_parts / self.productivity

    def __add__(self, other):
        """
        Перегрузка оператора сложения.
        Возвращает новый объект CNC_Machine с объединёнными характеристиками.
        """
        if isinstance(other, CNC_Machine):
            combined_machine = super().__add__(other)
            return CNC_Machine(
                combined_machine.productivity,
                combined_machine.cost,
                combined_machine.average_part_price,
                (self.automation_level + other.automation_level) / 2
            )
        return super().__add__(other)

    def __str__(self):
        return (f"CNC_Machine(productivity={self.productivity}, cost={self.cost}, "
                f"average_part_price={self.average_part_price}, automation_level={self.automation_level})")


# Пример использования
if __name__ == "__main__":
    # Создание объекта фрезерного станка
    milling_machine1 = MillingMachine(productivity=50, cost=100000, average_part_price=500, milling_precision=10)
    milling_machine2 = MillingMachine(productivity=70, cost=120000, average_part_price=550, milling_precision=15)

    # Создание объекта станка с ЧПУ
    cnc_machine1 = CNC_Machine(productivity=80, cost=200000, average_part_price=700, automation_level=90)
    cnc_machine2 = CNC_Machine(productivity=90, cost=250000, average_part_price=750, automation_level=95)

    # Сложение станков
    combined_milling_machine = milling_machine1 + milling_machine2
    combined_cnc_machine = cnc_machine1 + cnc_machine2

    print("Сложение фрезерных станков:")
    print(combined_milling_machine)

    print("\nСложение станков с ЧПУ:")
    print(combined_cnc_machine)
