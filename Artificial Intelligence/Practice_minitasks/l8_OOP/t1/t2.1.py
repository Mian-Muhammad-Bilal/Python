import taa1


class LivingThing:
    def __init__(self, alive):
        self.alive = alive


class Human(LivingThing):
    def __init__(self, alive, language_spoken, is_homo_sapien):
        LivingThing.__init__(self, alive)
        self.language_spoken = language_spoken
        self.is_homo_sapien = is_homo_sapien


class Superhero(taa1.Person, Human):

    def __init__(self, name, age, gender, alive, language_spoken, is_homo_sapien, superhero_name):
        taa1.Person.__init__(self, name, age, gender)
        self.name = name
        self.age = age
        self.gender = gender
        Human.__init__(self, alive, language_spoken, is_homo_sapien)
        self.superhero_name = superhero_name

    def save_the_day(self):
        print(f"{self.superhero_name} is saving the day!")

    def disply_info(self):
        print(f"Superhero Name: {self.superhero_name}")
        print(f"Alive: {'Yes' if self.alive else 'No'}")
        print(f"Language Spoken: {self.language_spoken}")
        print(f"Is Homo Sapien: {'Yes' if self.is_homo_sapien else 'No'}")


S1 = Superhero(name="Jerry", age="26", gender="male", alive=True,
               language_spoken="English", is_homo_sapien=True, superhero_name="Superman")

if __name__ == "__main__":
    S1.save_the_day()
    S1.disply_info()
