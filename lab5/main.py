from models import (Asset, Firewall, HardwareFirewall, SoftwareFirewall,
                    Antivirus)
 
 
def report(items):
    total = 0
    n = 0
    for item in items:
        n += 1
        value = item.check_time_ms()
        print(f"{n}. {item} → {value} мс")
        total += value
    print("Сумма:", round(total, 2), "мс; среднее:", round(total / n, 2), "мс")
    return total
 
 
def find_max(items):
    best = items[0]
    for item in items:
        if item.check_time_ms() > best.check_time_ms():
            best = item
    return best
 
 
print("=== Задание 3. Полиморфный метод ===")
fw = Firewall("fw-kornilov", 1000, 200, True)
hw = HardwareFirewall("fw-hw-kornilov", 1000, 500, True, 10)
sw = SoftwareFirewall("fw-sw-kornilov", 1000, 300, True, "Debian 12")
print("Firewall:", fw.check_time_ms())
print("HardwareFirewall:", hw.check_time_ms())
print("SoftwareFirewall:", sw.check_time_ms())
 
print()
print("=== Задание 4. report() и find_max() ===")
items = [
    SoftwareFirewall("fw-sw1-kornilov", 800, 400, True, "Windows Server"),
    Firewall("fw-kornilov-a", 1000, 150, True),
    HardwareFirewall("fw-hw1-kornilov", 2000, 1200, True, 40),
    Firewall("fw-kornilov-b", 500, 90, False),
    SoftwareFirewall("fw-sw2-kornilov", 300, 30, True, "Ubuntu 24.04"),
    HardwareFirewall("fw-hw2-kornilov", 600, 250, False, 10),
]
report(items)
print("Максимум:", find_max(items))
 
print()
print("=== Задание 5. Сравнение ===")
for x in sorted(items):
    print(x.rules, "-", x)
print("min:", min(items))
print("max:", max(items))
a = Firewall("fw-kornilov-c", 1000, 150, True)
b = HardwareFirewall("fw-hw3-kornilov", 700, 150, True, 20)
print("a == b:", a == b, "| a is b:", a is b)
print("a > b:", a > b)
print("a <= b:", a <= b)
 
print()
print("=== Задание 6. Утиная типизация ===")
mixed = items + [Antivirus("av-kornilov")]
report(mixed)
try:
    sorted(mixed)
except Exception as e:
    print("Ошибка сортировки:", type(e).__name__ + ":", e)
 
print()
print("=== Задание 7. Абстрактный класс ===")
try:
    Asset()
except TypeError as e:
    print("Ошибка:", e)
 
 
class Draft(Asset):
    def __str__(self):
        return "черновик"
 
 
try:
    Draft()
except TypeError as e:
    print("Ошибка:", e)
print("Обычные объекты создаются:", fw)
