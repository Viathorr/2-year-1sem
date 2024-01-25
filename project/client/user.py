class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def change_name(self, new_name):
        self.name = new_name
