# auth.py

class User:
    users_db = {
        "admin": {"password": "admin123", "role": "Admin"},
        "user": {"password": "user123", "role": "User"}
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = None
        self.authenticate()

    def authenticate(self):
        user = self.users_db.get(self.username)
        if user and user["password"] == self.password:
            self.role = user["role"]
        else:
            print("Invalid credentials!")

    def is_admin(self):
        return self.role == "Admin"

    def get_role(self):
        return self.role
