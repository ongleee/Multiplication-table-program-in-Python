class tank:
    def __init__(self , name , ammo):
        self.name = name
        self.ammo = ammo
first_tank = tank('Henry' , 10)
print(first_tank.name)

second_tank = tank('GG' , 4)
print(second_tank.name)