class Glassware:
    def __init__(self,glassware_type):
        self.glassware_type = glassware_type

class Beaker(Glassware):
    def __init__(self,glassware_type,beaker_no):
        super().__init__(glassware_type)
        self.beaker_no = beaker_no

class Tray:
    def __init__(self,glassware_type):
        self.glassware_type = glassware_type
        self.beakers = [Beaker(self.glassware_type, i + 1) for i in range(5)]
    def display_beakers(self):
        print("Tray has: ")
        for beaker in self.beakers:
            print(f"Beaker #: {beaker.beaker_no}; Type: {beaker.glassware_type}")

if __name__ == "__main__":
    tray = Tray(glassware_type="Standard Beakers")
    tray.display_beakers()
