class Octopus:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


def main():
    octopus1 = Octopus("Octavio", 3)
    octopus2 = Octopus("Octavio", 5)

    octopus1.birthday()

    print(octopus1.get_age())
    print(octopus2.get_age())


if __name__ == "__main__":
    main()