class Firewall:
    """Межсетевой экран: фильтрует сетевой трафик по набору правил."""
 
    count = 0
    type_name = "Межсетевой экран"  # название типа, переопределяется в подклассах
 
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
 
    def __str__(self):
        state = "активен" if self.active else "отключён"
        return (f"{self.type_name} {self.name}: правил {self.rules} "
                f"из {self.max_rules}, {state}")
 
 
class HardwareFirewall(Firewall):
    """Аппаратный межсетевой экран — это межсетевой экран, выполненный в виде
    отдельного устройства, поэтому у него есть всё, что и у обычного экрана,
    плюс пропускная способность канала."""
 
    type_name = "Аппаратный межсетевой экран"
 
    def __init__(self, name, max_rules, rules, active, throughput_gbps):
        super().__init__(name, max_rules, rules, active)
        if throughput_gbps < 1 or throughput_gbps > 100:
            raise ValueError(
                f"throughput_gbps = {throughput_gbps}: допустимо от 1 до 100")
        self.throughput_gbps = throughput_gbps
 
    def max_sessions(self):
        return self.throughput_gbps * 50000
 
    def __str__(self):
        return super().__str__() + f", {self.throughput_gbps} Гбит/с"
 
 
class SoftwareFirewall(Firewall):
    """Программный межсетевой экран — это межсетевой экран, установленный как
    программа в операционной системе, поэтому к обычным полям добавлено
    название ОС."""
 
    type_name = "Программный межсетевой экран"
 
    def __init__(self, name, max_rules, rules, active, os_name):
        super().__init__(name, max_rules, rules, active)
        if os_name == "":
            raise ValueError("os_name: название ОС не может быть пустым")
        self.os_name = os_name
 
    def install_command(self):
        return f"install fw on {self.os_name}"
 
    def __str__(self):
        return super().__str__() + f", ОС {self.os_name}"
 
 
class HistoryMixin:
    """Примесь: ведёт журнал действий в списке self.history."""
 
    def log(self, message):
        if not hasattr(self, "history"):
            self.history = []
        self.history.append(message)
 
    def show_history(self):
        for i, line in enumerate(getattr(self, "history", []), 1):
            print(f"{i}. {line}")
 
 
class LoggedHardwareFirewall(HistoryMixin, HardwareFirewall):
    """Аппаратный экран, который записывает в журнал добавление правил."""
 
    def add_rules(self, n):
        super().add_rules(n)
        self.log(f"добавлено правил: {n}")
