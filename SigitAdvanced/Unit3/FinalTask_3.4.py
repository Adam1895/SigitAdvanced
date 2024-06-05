import string

class UsernameContainsIllegalCharacter(Exception):
    """
    Exception raised when the username contains an illegal character.

    Attributes:
        username (str): The username that contains the illegal character.
        illegal_char (str): The illegal character found in the username.
        index (int): The index of the illegal character in the username.
    """
    def __init__(self, username, illegal_char, index):
        self.username = username
        self.illegal_char = illegal_char
        self.index = index

    def __str__(self):
        return f"The username contains an illegal character \"{self.illegal_char}\" at index {self.index}"

class UsernameTooShort(Exception):
    """Exception raised when the username is too short."""
    def __str__(self):
        return "The username is too short"

class UsernameTooLong(Exception):
    """Exception raised when the username is too long."""
    def __str__(self):
        return "The username is too long"

class PasswordMissingCharacter(Exception):
    """Base exception for missing character types in the password."""
    def __str__(self):
        return "The password is missing a character"

class PasswordMissingUppercase(PasswordMissingCharacter):
    """Exception raised when the password is missing an uppercase character."""
    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    """Exception raised when the password is missing a lowercase character."""
    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    """Exception raised when the password is missing a digit."""
    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    """Exception raised when the password is missing a special character."""
    def __str__(self):
        return super().__str__() + " (Special)"

class PasswordTooShort(Exception):
    """Exception raised when the password is too short."""
    def __str__(self):
        return "The password is too short"

class PasswordTooLong(Exception):
    """Exception raised when the password is too long."""
    def __str__(self):
        return "The password is too long"

def check_input(username, password):
    """
    Checks if the given username and password meet the requirements.

    Args:
        username (str): The username to be checked.
        password (str): The password to be checked.

    Raises:
        UsernameContainsIllegalCharacter: If the username contains an illegal character.
        UsernameTooShort: If the username is too short.
        UsernameTooLong: If the username is too long.
        PasswordTooShort: If the password is too short.
        PasswordTooLong: If the password is too long.
        PasswordMissingUppercase: If the password is missing an uppercase character.
        PasswordMissingLowercase: If the password is missing a lowercase character.
        PasswordMissingDigit: If the password is missing a digit.
        PasswordMissingSpecial: If the password is missing a special character.
    """
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()
    for i, char in enumerate(username):
        if not (char.isalnum() or char == '_'):
            raise UsernameContainsIllegalCharacter(username, char, i)

    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()
    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase()
    if not any(char.islower() for char in password):
        raise PasswordMissingLowercase()
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigit()
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()

def main():
    """
    Main function that demonstrates the usage of the check_input function and handles user input.
    """
    try:
        check_input("1", "2")
    except UsernameTooShort as e:
        print(e)

    try:
        check_input("0123456789ABCDEFG", "2")
    except UsernameTooLong as e:
        print(e)

    try:
        check_input("A_a1.", "12345678")
    except UsernameContainsIllegalCharacter as e:
        print(e)

    try:
        check_input("A_1", "2")
    except PasswordTooShort as e:
        print(e)

    try:
        check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    except PasswordTooLong as e:
        print(e)

    try:
        check_input("A_1", "abcdefghijklmnop")
    except PasswordMissingUppercase as e:
        print(e)

    try:
        check_input("A_1", "ABCDEFGHIJLKMNOP")
    except PasswordMissingLowercase as e:
        print(e)

    try:
        check_input("A_1", "ABCDEFGhijklmnop")
    except PasswordMissingDigit as e:
        print(e)

    try:
        check_input("A_1", "4BCD3F6h1jk1mn0p")
    except PasswordMissingSpecial as e:
        print(e)

    try:
        check_input("A_1", "4BCD3F6.1jk1mn0p")
    except Exception as e:
        print(e)
    else:
        print("OK")

    print("\n==================================================\n")

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
                PasswordMissingUppercase, PasswordMissingLowercase, PasswordMissingDigit,
                PasswordMissingSpecial, PasswordTooShort, PasswordTooLong) as e:
            print(e)

if __name__ == "__main__":
    main()