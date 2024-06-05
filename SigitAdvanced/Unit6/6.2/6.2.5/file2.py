from file1 import GreetingCard

class BirthdayCard(GreetingCard):
    def __init__(self, sender_age=0):
        super().__init__()
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print(f"Happy birthday! {self._sender} (the sender) is {self._sender_age} years old.")