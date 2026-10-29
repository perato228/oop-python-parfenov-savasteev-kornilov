from models import Firewall
 
print("=== Задание 3. Создание объектов ===")
f1 = Firewall("fw-kornilov", 1000, 120, True)
f2 = Firewall("fw-edge", 500, 480, False)
for f in (f1, f2):
    print("name:", f.name, "| max_rules:", f.max_rules,
          "| rules:", f.rules, "| active:", f.active)
print("Создано экранов (Firewall.count):", Firewall.count)
 
print()
print("=== Задание 4. Проверка входных данных ===")
try:
    Firewall("", 100, 0, True)
except ValueError as e:
    print("Ошибка:", e)
try:
    Firewall("fw-test", 5000, 0, True)
except ValueError as e:
    print("Ошибка:", e)
try:
    Firewall("fw-test", 100, 150, True)
except ValueError as e:
    print("Ошибка:", e)
print("Firewall.count после неудачных попыток:", Firewall.count)
 
print()
print("=== Задание 5. Методы и __str__ ===")
print(f1)
f1.add_rules(30)
print(f1)
print("Можно добавить правил:", f1.free_rules())
try:
    f2.add_rules(50)
except ValueError as e:
    print("Ошибка:", e)
 
print()
print("=== Задание 6. Свойство rules ===")
print("Чтение через свойство:", f1.rules)
f1.rules = 200
print("После присваивания 200:", f1.rules)
try:
    f1.rules = 1500
except ValueError as e:
    print("Ошибка:", e)
 
print()
print("=== Задание 7. Итог ===")
f3 = Firewall("fw-dmz", 100, 10, True)
print(f3)
print("Firewall.count =", Firewall.count)
