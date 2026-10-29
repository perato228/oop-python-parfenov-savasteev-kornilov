class Firewall:
    """Межсетевой экран: фильтрует сетевой трафик по набору правил.
    Объект хранит имя экрана, максимальное число правил, сколько правил
    уже настроено и включён ли экран."""
 
    count = 0  # атрибут класса: сколько экранов создано
 
    def __init__(self, name, max_rules, rules, active):
        if name == "":
            raise ValueError("name: имя межсетевого экрана не может быть пустым")
        if max_rules < 10 or max_rules > 2000:
            raise ValueError(f"max_rules = {max_rules}: допустимо от 10 до 2000")
        self.name = name
        self.max_rules = max_rules
        self.active = active
        self.rules = rules  # присваивание вызывает сеттер (проверка 0..max_rules)
        Firewall.count += 1  # только после всех проверок
 
    @property
    def rules(self):
        return self._rules
 
    @rules.setter
    def rules(self, value):
        if value < 0 or value > self.max_rules:
            raise ValueError(f"rules = {value}: допустимо от 0 до {self.max_rules}")
        self._rules = value
 
    def add_rules(self, n):
        """Метод-изменение: добавляет n новых правил."""
        if n <= 0:
            raise ValueError(f"n = {n}: число правил должно быть больше 0")
        if n > self.free_rules():
            raise ValueError(f"n = {n}: свободно только {self.free_rules()} правил")
        self.rules = self.rules + n  # через свойство
 
    def free_rules(self):
        """Расчётный метод: сколько правил ещё можно добавить."""
        return self.max_rules - self.rules
 
    def __str__(self):
        state = "активен" if self.active else "отключён"
        return (f"Межсетевой экран {self.name}: правил {self.rules} "
                f"из {self.max_rules}, {state}")
