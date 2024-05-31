"""
10-4. Guest
사용자에게 이름을 묻는 메시지를 표시하는 프로그램을 작성합니다. 사용자가 응답하면 guest.txt라는 파일에 이름을 기록합니다.
"""

from pathlib import Path

path = Path('guest.txt')

name = input("너의 이름이 뭐니? ")
path.write_text(name)
