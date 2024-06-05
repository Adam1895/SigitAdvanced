class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        years_left = 18 - self.age
        return f"Your age is under 18. You will be able to attend Ido's birthday in {years_left} years."

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(int(age))
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)

# Test the function with different ages
send_invitation("John", 17)
send_invitation("Alice", 20)