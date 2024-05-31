import json
from pathlib import Path

path = Path('txt/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")
