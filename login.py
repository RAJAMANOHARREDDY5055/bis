# login.py

def login(username, password):
    """
    Simple login function that checks username and password against hardcoded values.
    """
    # Hardcoded credentials for simplicity
    correct_username = "admin"
    correct_password = "12345"

    if username == correct_username and password == correct_password:
        return "Login successful!"
    else:
        return "Invalid username or password."

# Example usage (optional for testing)
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    print(login(user, pwd))
