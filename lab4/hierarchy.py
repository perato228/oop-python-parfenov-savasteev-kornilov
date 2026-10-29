from models import Firewall, HardwareFirewall, SoftwareFirewall
 
b = Firewall("fw-kornilov", 1000, 100, True)
s1 = HardwareFirewall("fw-hw-kornilov", 800, 100, True, 10)
s2 = SoftwareFirewall("fw-sw-kornilov", 300, 30, True, "Debian 12")
 
print("1 ", isinstance(s1, Firewall))
print("2 ", isinstance(b, HardwareFirewall))
print("3 ", isinstance(s2, HardwareFirewall))
print("4 ", issubclass(SoftwareFirewall, Firewall))
print("5 ", issubclass(Firewall, Firewall))
print("6 ", type(s1) == Firewall)
print("7 ", HardwareFirewall.__bases__)
print("8 ", HardwareFirewall.__mro__)
print("9 ", Firewall.count)
try:
    b.max_sessions()
except Exception as e:
    print("10", type(e).__name__ + ":", e)
