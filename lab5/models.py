from abc import ABC, abstractmethod
 
 
class Asset(ABC):
    """Абстрактный интерфейс: любой объект должен уметь считать время
    проверки пакета и выводить себя в виде строки."""
 
    @abstractmethod
    def check_time_ms(self):
        pass
 
    @abstractmethod
    def __str__(self):
        pass
 
 
class Firewall(Asset):
    """Межсетевой экран: фильтрует сетевой трафик по набору правил."""
 
    count = 0
    type_name = "Межсетевой экран"
 
    def __init__(self, name, max_rules, rules, active):
        if name == "":
            raise ValueError("name: имя межсетевого экрана не может быть пустым")
        if max_rules < 10 or max_rules > 2000:
            raise ValueError(f"max_rules = {max_rules}: допустимо от 10 до 2000")
        self.name = name
        self.max_rules = max_rules
        self.active = active
        self.rules = rules
        Firewall.count += 1
 
    @property
    def rules(self):
        return self._rules
 
    @rules.setter
    def rules(self, value):
        if value < 0 or value > self.max_rules:
            raise ValueError(f"rules = {value}: допустимо от 0 до {self.max_rules}")
        self._rules = value
 
    def add_rules(self, n):
        if n <= 0:
            raise ValueError(f"n = {n}: число правил должно быть больше 0")
        if n > self.free_rules():
            raise ValueError(f"n = {n}: свободно только {self.free_rules()} правил")
        self.rules = self.rules + n
 
    def free_rules(self):
        return self.max_rules - self.rules
 
    def check_time_ms(self):
        """Полиморфный метод: время проверки одного пакета, мс."""
        return round(0.01 * self.rules, 2)
 
    def __eq__(self, other):
        return self.rules == other.rules
 
    def __lt__(self, other):
        return self.rules < other.rules
 
    def __le__(self, other):
        return self.rules <= other.rules
 
    def __add__(self, other):
        return self.check_time_ms() + other.check_time_ms()
 
    def __radd__(self, other):  # sum() начинает с 0: 0 + объект
        return other + self.check_time_ms()
 
    def __str__(self):
        state = "активен" if self.active else "отключён"
        return (f"{self.type_name} {self.name}: правил {self.rules} "
                f"из {self.max_rules}, {state}")
 
 
class HardwareFirewall(Firewall):
    """Аппаратный межсетевой экран — экран в виде отдельного устройства."""
 
    type_name = "Аппаратный межсетевой экран"
 
    def __init__(self, name, max_rules, rules, active, throughput_gbps):
        super().__init__(name, max_rules, rules, active)
        if throughput_gbps < 1 or throughput_gbps > 100:
            raise ValueError(
                f"throughput_gbps = {throughput_gbps}: допустимо от 1 до 100")
        self.throughput_gbps = throughput_gbps
 
    def max_sessions(self):
        return self.throughput_gbps * 50000
 
    def check_time_ms(self):
        return round(0.001 * self.rules, 2)
 
    def __str__(self):
        return super().__str__() + f", {self.throughput_gbps} Гбит/с"
 
 
class SoftwareFirewall(Firewall):
    """Программный межсетевой экран — экран-программа в операционной системе."""
 
    type_name = "Программный межсетевой экран"
 
    def __init__(self, name, max_rules, rules, active, os_name):
        super().__init__(name, max_rules, rules, active)
        if os_name == "":
            raise ValueError("os_name: название ОС не может быть пустым")
        self.os_name = os_name
 
    def install_command(self):
        return f"install fw on {self.os_name}"
 
    def check_time_ms(self):
        return round(super().check_time_ms() * 2 + 1, 2)
 
    def __str__(self):
        return super().__str__() + f", ОС {self.os_name}"
 
 
class Antivirus:
    """Посторонний класс: не наследует Firewall («утиная» типизация)."""
 
    def __init__(self, name):
        self.name = name
 
    def check_time_ms(self):
        return 5
 
    def __str__(self):
        return f"Антивирус {self.name}"
