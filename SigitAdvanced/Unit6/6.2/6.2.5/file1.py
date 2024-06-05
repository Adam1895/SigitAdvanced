class GreetingCard:
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch'):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f"Greetings from {self._sender} to {self._recipient}.")