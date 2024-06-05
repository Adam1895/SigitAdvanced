class Animal:
    """
    A class representing an animal in the zoo.
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        Initialize an Animal instance.

        Args:
            name (str): The name of the animal.
            hunger (int, optional): The hunger level of the animal. Default is 0.
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Get the name of the animal.

        Returns:
            str: The name of the animal.
        """
        return self._name

    def is_hungry(self):
        """
        Check if the animal is hungry.

        Returns:
            bool: True if the animal is hungry, False otherwise.
        """
        return self._hunger > 0

    def feed(self):
        """
        Feed the animal, reducing its hunger level by 1 if it's greater than 0.
        """
        self._hunger -= 1 if self._hunger > 0 else 0

    def talk(self):
        """
        Make the animal talk. This method should be overridden by subclasses.
        """
        pass


class Dog(Animal):
    """
    A class representing a dog, which is a type of animal.
    """
    def talk(self):
        """
        Make the dog bark.
        """
        print("woof woof")

    def fetch_stick(self):
        """
        Make the dog fetch a stick.
        """
        print("There you go, sir!")


class Cat(Animal):
    """
    A class representing a cat, which is a type of animal.
    """
    def talk(self):
        """
        Make the cat meow.
        """
        print("meow")

    def chase_laser(self):
        """
        Make the cat chase a laser.
        """
        print("Meeeeow")


class Skunk(Animal):
    """
    A class representing a skunk, which is a type of animal.
    """
    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initialize a Skunk instance.

        Args:
            name (str): The name of the skunk.
            hunger (int, optional): The hunger level of the skunk. Default is 0.
            stink_count (int, optional): The number of times the skunk can stink. Default is 6.
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        Make the skunk hiss.
        """
        print("tsssss")

    def stink(self):
        """
        Make the skunk stink.
        """
        print("Dear lord!")


class Unicorn(Animal):
    """
    A class representing a unicorn, which is a type of animal.
    """
    def talk(self):
        """
        Make the unicorn say something fancy.
        """
        print("Good day, darling")

    def sing(self):
        """
        Make the unicorn sing.
        """
        print("I'm not your toy...")


class Dragon(Animal):
    """
    A class representing a dragon, which is a type of animal.
    """
    def __init__(self, name, hunger=0, color="Green"):
        """
        Initialize a Dragon instance.

        Args:
            name (str): The name of the dragon.
            hunger (int, optional): The hunger level of the dragon. Default is 0.
            color (str, optional): The color of the dragon. Default is "Green".
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        Make the dragon roar.
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        Make the dragon breathe fire.
        """
        print("$@#$#@$")


def main():
    """
    The main function of the program.
    """
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky"),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()
        print(type(animal).__name__, animal.get_name())
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
        print("\n")

    print(f"Zoo name: {Animal.zoo_name}")


if __name__ == "__main__":
    main()