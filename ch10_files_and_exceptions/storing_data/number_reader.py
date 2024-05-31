import json

from pathlib import Path

path = Path('txt/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)