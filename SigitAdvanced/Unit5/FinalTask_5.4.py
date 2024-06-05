def check_id_valid(id_number: int) -> bool:
    """
    Checks if a given ID number is valid.

    Args:
        id_number (int): The ID number.

    Returns:
        bool: True if the ID number is valid, False otherwise.
    """
    if not (0 <= id_number <= 999999999):
        return False

    else:
        digits = [int(digit) for digit in str(id_number)]
        multipliers = [1, 2] * 4 + [1]
        weighted_digits = [a * b for a, b in zip(digits, multipliers)]
        summed_digits = sum(digit if digit <= 9 else sum(int(d) for d in str(digit)) for digit in weighted_digits)
        return (summed_digits % 10 == 0)


class IDIterator:
    max_id = 999999999

    def __init__(self, id: int):
        """
        Initialize the IDIterator object.

        Args:
            id (int): The starting ID number.

        Raises:
            ValueError: If the ID number is not within the valid range.
        """
        if not (0 <= id <= self.max_id):
            raise ValueError(f"ID number must be between 0 and {self.max_id}")

        self._id = id

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            IDIterator: The instance of the IDIterator class.
        """
        return self

    def __next__(self) -> int:
        """
        Returns the next valid ID number.

        Returns:
            int: A valid ID number.

        Raises:
            StopIteration: If there are no more valid ID numbers within the range.
        """
        while self._id <= self.max_id:
            if check_id_valid(self._id):
                result = self._id
                self._id += 1
                return result
            self._id += 1
        raise StopIteration


def id_generator(id: int) -> int:
    """
    Generator function that yields valid ID numbers.

    Args:
        id (int): Starting ID number.

    Yields:
        int: A valid ID number.

    Raises:
        ValueError: If the ID number is not within the valid range.
    """
    max_id = 999999999

    if not (0 <= id <= max_id):
        raise ValueError(f"ID number must be between 0 and {max_id}")
    else:
        while id <= max_id:
            if check_id_valid(id):
                yield id
                id += 1
            else:
                id += 1


if __name__ == "__main__":
    print(check_id_valid(123456780))
    print(check_id_valid(123456782))

    id_input = int(input("Enter ID: "))
    gen_or_iter = input("Generator or Iterator? (gen/it)? ")

    try:
        if gen_or_iter == "it":
            id_iterator = IDIterator(id_input)
            for i in range(10):
                print(next(id_iterator))
        elif gen_or_iter == "gen":
            id_gen = id_generator(id_input)
            for i in range(10):
                print(next(id_gen))
        else:
            print("Invalid, please re-run")
    except ValueError as e:
        print(e)

