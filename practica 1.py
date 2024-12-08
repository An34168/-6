class Machine:
    def __init__(self, productivity, cost, average_part_price):
        
        self.productivity = productivity
        self.cost = cost
        self.average_part_price = average_part_price

    def parts_for_breakeven(self):
       
        return self.cost / self.average_part_price


class MillingMachine(Machine):
    def __init__(self, productivity, cost, average_part_price, milling_precision):
        super().__init__(productivity, cost, average_part_price)
        self.milling_precision = milling_precision

    def payback_time(self, fixed_part_price):
        total_parts = self.cost / fixed_part_price
        return total_parts / self.productivity


class CNC_Machine(Machine):
    def __init__(self, productivity, cost, average_part_price, automation_level):
        super().__init__(productivity, cost, average_part_price)
        self.automation_level = automation_level

    def payback_time(self, fixed_part_price):
        total_parts = self.cost / fixed_part_price
        return total_parts / self.productivity


# Пример использования
if __name__ == "__main__":
    # Создание объекта фрезерного станка
    milling_machine = MillingMachine(productivity=50, cost=100000, average_part_price=500, milling_precision=10)
    print("Фрезерный станок:")
    print(f"Количество деталей для окупаемости: {milling_machine.parts_for_breakeven()}")
    print(f"Время окупаемости: {milling_machine.payback_time(450)} часов")

    # Создание объекта станка с ЧПУ
    cnc_machine = CNC_Machine(productivity=70, cost=200000, average_part_price=700, automation_level=90)
    print("\nСтанок с ЧПУ:")
    print(f"Количество деталей для окупаемости: {cnc_machine.parts_for_breakeven()}")
    print(f"Время окупаемости: {cnc_machine.payback_time(650)} часов")
