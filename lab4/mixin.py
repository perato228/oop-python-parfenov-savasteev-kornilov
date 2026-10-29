from models import HardwareFirewall, HistoryMixin, LoggedHardwareFirewall
 
fw = LoggedHardwareFirewall("fw-log-kornilov", 1000, 100, True, 10)
fw.add_rules(20)
fw.add_rules(5)
fw.show_history()
print(LoggedHardwareFirewall.__mro__)
 
 
class Swapped(HardwareFirewall, HistoryMixin):
    pass
 
 
print(Swapped.__mro__)
