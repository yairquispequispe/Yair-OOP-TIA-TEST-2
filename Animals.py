class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} hace: {self.sound}")


class Vaca(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed


class Perro(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed


vaca1 = Vaca("Lola", "MUUUUU", "Holando-Argentino")
perro1 = Perro("Firulais", "GUAU GUAU", "Golden Retriever")

vaca1.make_sound()
perro1.make_sound()

    
