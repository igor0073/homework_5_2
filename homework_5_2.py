class Building:
    def __init__(self, number_of_floors, building_type):
        self.number_of_floors = number_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.building_type == other.building_type


b1 = Building(12, 'brick_building')
b2 = Building(12, 'panel_building')

print(b1.number_of_floors, b1.building_type)
print(b2.number_of_floors, b2.building_type)
print(b1 == b2)