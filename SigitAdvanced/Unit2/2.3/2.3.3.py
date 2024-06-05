class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio", age=0):
        self._name = name
        self._age = age
        Octopus.count_animals += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


def main():
    octopus1 = Octopus("Inky", 3)
    octopus2 = Octopus(age=5)

    print("octupus 1 name: ", octopus1.get_name())
    print("octupus 2 name: ", octopus2.get_name())

    print("octupus 1 age: ", octopus1.get_age())
    print("octupus 2 age: ", octopus2.get_age())

    octopus1.set_name("Blinky")

    print("octupus 1 new name: ", octopus1.get_name())

    octopus1.birthday()
    print("octupus 1 new age: ", octopus1.get_age())


    print("count animals: ", Octopus.count_animals)

if __name__ == "__main__":
    main()