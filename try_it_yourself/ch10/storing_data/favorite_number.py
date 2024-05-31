"""
10-11. Favorite Number
사용자의 좋아하는 숫자를 파일에 저장하세요. json.dumps() 사용
"I know your favorite number! It's ___." 메시지도 출력하세요.
"""

import json
from pathlib import Path

num = input("What is your favorite number? ")

path = Path('favorite_number.json')
contents = json.dumps(num)
path.write_text(contents)

print(f"I know your favorite number! It's {num}.")
