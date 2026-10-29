from models import Firewall, HardwareFirewall, SoftwareFirewall
 
items = [
    Firewall("fw-kornilov", 1000, 200, True),
    HardwareFirewall("fw-hw-kornilov", 1000, 500, True, 10),
    SoftwareFirewall("fw-sw-kornilov", 1000, 300, True, "Debian 12"),
]
a, b, c = items
print("a + b =", a + b)
print("sum(items) =", round(sum(items), 2))
print("вручную    =", round(a.check_time_ms() + b.check_time_ms() + c.check_time_ms(), 2))
