class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

def make_sound(self, vaca, perro):
    self.vaca = vaca
    self.perro = perro
    
class Vaca(Animal):
    def __init__(self, name, sound, vaca):
        super().__init__(name, sound)
        self.vaca = vaca
        print("MUUUUU")
class Perro(Animal):
    def __init__(self, name, sound, perro):
        super().__init__(name, sound)
        self.perro = perro
        print("GUAF GUAF")

    