from models import Firewall, HardwareFirewall, SoftwareFirewall
 
print("=== Задание 3. Подкласс 1: HardwareFirewall ===")
hw = HardwareFirewall("fw-hw-kornilov", 1000, 200, True, 10)
hw.add_rules(50)  # унаследованный метод-изменение
print(hw)
print("Можно добавить правил:", hw.free_rules())  # унаследованный расчётный
print("Макс. сессий:", hw.max_sessions())  # собственный метод
try:
    HardwareFirewall("fw-hw-bad", 1000, 200, True, 150)
except ValueError as e:
    print("Ошибка:", e)
 
print()
print("=== Задание 4. Подкласс 2: SoftwareFirewall ===")
sw = SoftwareFirewall("fw-sw-kornilov", 500, 40, True, "Ubuntu 24.04")
print(sw)
print(sw.install_command())
try:
    SoftwareFirewall("fw-sw-bad", 5, 0, True, "Linux")  # ошибка в поле базового класса
except ValueError as e:
    print("Ошибка базового поля:", e)
try:
    SoftwareFirewall("fw-sw-bad", 500, 0, True, "")  # ошибка в поле подкласса
except ValueError as e:
    print("Ошибка поля подкласса:", e)
 
print()
print("=== Задание 5. __str__ ===")
print(hw)
print(sw)
 
print()
print("=== Задание 7. Демонстрация иерархии ===")
items = [
    Firewall("fw-kornilov", 1000, 120, True),
    HardwareFirewall("fw-hw1-kornilov", 800, 100, True, 10),
    HardwareFirewall("fw-hw2-kornilov", 600, 50, False, 40),
    SoftwareFirewall("fw-sw1-kornilov", 300, 30, True, "Windows Server"),
    SoftwareFirewall("fw-sw2-kornilov", 200, 90, True, "Debian 12"),
]
stat = {}
for obj in items:
    print(obj)
    if isinstance(obj, HardwareFirewall):
        print("   макс. сессий:", obj.max_sessions())
    if isinstance(obj, SoftwareFirewall):
        print("   команда:", obj.install_command())
    name = type(obj).__name__
    stat[name] = stat.get(name, 0) + 1
print()
for name in stat:
    print(name, "-", stat[name])
