from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass

class PHSensor(Sensor):
    def get_data(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_data(self):
        return "[Temperature Sensor] Reading: 24.5°C"

print("--- Lab Inventory System ---")
sensor1 = PHSensor()
sensor2 = TempSensor()
print(sensor1.get_data())
print(sensor2.get_data())
print("\n----------------------------")

#my_sensor = Sensor()
