import json

from pathlib import Path

numbers = [2, 3, 5, 7, 11, 13]

path = Path('txt/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)  # 텍스트를 파일에 쓸 때와 같은 방식. json도 알고보면 str이다.

print(type(contents))  # <class 'str'>
