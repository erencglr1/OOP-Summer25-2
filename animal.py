class Animal:
    def __init__(self, name, group, legs, skills):
        self.name = name
        self.group = group
        self.legs = legs
        self.skills = skills

animals = [
    Animal("Doggy", "Mammals", 4, ["Running", "Swimming", "Barking"]),
    Animal("Parrot", "Birds", 2, ["Flying", "Singing"]),
    Animal("Elephant", "Mammals", 4, ["Trunk usage", "Swimming", "Heavy lifting"]),
    Animal("Cow", "Mammals", 4, ["Grazing", "Milk production"]),
    Animal("Snake", "Reptiles", 0, ["Slithering", "Hunting"])
]

for a in animals:
    print(a.name, "-", a.group, "-", a.legs, "legs", "- Skills:", ", ".join(a.skills))









