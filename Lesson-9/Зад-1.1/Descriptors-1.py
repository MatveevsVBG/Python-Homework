class StrValidator:
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"Неправильный ввод данных - переменная "
                            f"{self.my_attr} должна быть строкой")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = StrValidator()
    surname = StrValidator()
    position = StrValidator()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self. surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


work = Position('John', 'Smith', 'engineer', 20000, 5000)
print(f'{work.get_full_name()} - {work.position} - {work.get_total_income()}')