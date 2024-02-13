class LivingThing:
    def __init__(self, alive):
        self.alive = alive


class Human(LivingThing):
    def __init__(self, alive, language_spoken, is_homo_sapien):
        super().__init__(alive)
        self.language_spoken = language_spoken
        self.is_homo_sapien = is_homo_sapien


class Superhero(Human):
    def __init__(self, name, age, gender, language_spoken, is_homo_sapien):
        # Assuming a Superhero is both a Human and a Person
        super().__init__(alive=True, language_spoken=language_spoken,
                         is_homo_sapien=is_homo_sapien)
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        print(
            f"Language Spoken: {self.language_spoken}, Is Homo Sapien: {self.is_homo_sapien}")

    def save_the_day(self):
        print(f"{self.name} is saving the day!")


# Create an instance of Superhero
superhero = Superhero(name="Captain Marvel", age=30, gender="Female",
                      language_spoken="English", is_homo_sapien=True)

# Call display_info() and save_the_day() methods
print("\nSuperhero Information:")
superhero.display_info()
superhero.save_the_day()
