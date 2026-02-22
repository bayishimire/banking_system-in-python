class system:

    store = []

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login(self, password):
        for user in system.store:
            if user["name"] == self.name and user["password"] == password:
                return True
        return False

    def register(self, name, password):

        # Check if user already exists
        for user in system.store:
            if user["name"] == name:
                print(f"{name} already exists")
                return

        # Register new user
        system.store.append({
            "name": name,
            "password": password
        })

        print("Successful registration")
        print(system.store)