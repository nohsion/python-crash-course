"""
10-13. User Dictionary
remember_me.py 예제 참고
사용자 이름 외에 두 가지 정보를 더 요청하고 수집한 모든 정보를 dictionary에 저장하세요.
json.dumps()를 사용하여 이 dictionary을 파일에 쓰고 json.loads()를 사용하여 다시 읽습니다.
"""
import json
from pathlib import Path

def get_stored_userinfo(path):
    """Get stored userinfo if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_userinfo(path) -> dict:
    """Get information from a new user."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    location = input("Where are you from? ")

    user_info: dict = {
        'username': username,
        'age': age,
        'location': location
    }

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user(path):
    """Greet the user by name, and state what we know about them."""
    userinfo = get_stored_userinfo(path)
    if userinfo:
        print(f"Welcome back, {userinfo.get('username')}!")
        print(f"We know you are {userinfo.get('age')} years old, and you are from {userinfo.get('location')}.")
    else:
        userinfo = get_new_userinfo(path)
        print(f"We'll remember you when you come back, {userinfo.get('username')}!")


userinfo_path = Path('userinfo.json')
greet_user(userinfo_path)
