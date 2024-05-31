"""
10-12. Favorite Number Remembered
10-11 작성한 두 프로그램을 하나의 파일로 합치세요.
번호가 이미 저장되어 있으면 저장된 숫자를 출력하고,
그렇지 않으면 사용자에게 숫자를 물어 새로운 숫자를 저장하세요.
"""

import json
from pathlib import Path

path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    num = input("What is your favorite number? ")
    contents = json.dumps(num)
    path.write_text(contents)
    print(f"제가 기억하고 있을게요. {num}이(가) 좋아하는 숫자군요.")
else:
    num = json.loads(contents)
    print(f"좋아하는 숫자를 알고 있어요! {num} 이요!")
