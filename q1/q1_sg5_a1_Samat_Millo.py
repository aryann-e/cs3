class Hero:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def take_damage(self,amt):
        self.hp -= amt
        
arthur = Hero("Arthur",100)
morgana = Hero("Morgana",100)
arthur.take_damage(10)

print(f"{arthur.name}: {arthur.hp} HP")
print(f"{morgana.name}: {morgana.hp} HP")
