class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = int(floors)

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor > self.floors or new_floor < 1:
            print(f'В доме "{self.name}" этажа №{new_floor} не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.floors}')

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __gt__(self, other):
        return self.floors > other.floors

    def __ge__(self, other):
        return self.floors >= other.floors

    def __ne__(self, other):
        return self.floors != other.floors and self.name != other.name

    def __add__(self, other):
        self.floors += other
        return  self

    def __radd__(self, other):
        self.floors += other
        return self

    def __iadd__(self, other):
        self.floors += other
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
