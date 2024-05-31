import json
from pathlib import Path
"""
하나의 함수는 단 하나의 일을 해야 한다. (single, clear purpose)
그러면 유지보수와 확장이 용이한 코드가 된다.
"""


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user(path):
    """Greet the user by name."""
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


username_path = Path('txt/username.json')
greet_user(username_path)
