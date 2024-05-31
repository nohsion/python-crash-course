"""
10-14. Verify User
remember_me.py의 최종 목록은 사용자가 이미 사용자 아이디를 입력했거나 프로그램이 처음 실행 중이라고 가정합니다.
현재 사용자가 프로그램을 마지막으로 사용한 사람이 아닌 경우 수정해야 합니다.
greet_user()에서 환영 메시지를 인쇄하기 전에 사용자에게 올바른 사용자 이름인지 물어보세요.
그렇지 않은 경우 get_new_username()을 호출하여 올바른 사용자 아이디를 얻습니다.
"""

from pathlib import Path
import json


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
    if not username:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
        return

    correct = input(f"Are you {username}? (y/n) ")
    if correct == 'y':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


username_path = Path('username.json')
greet_user(username_path)
