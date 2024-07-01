from users.User import User

class PremiumUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)