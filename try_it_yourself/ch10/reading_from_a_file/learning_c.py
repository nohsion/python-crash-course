"""
10-2. Learning C
replace() 메서드를 사용하여 문자열의 모든 단어를 다른 단어로 바꿀 수 있습니다.
방금 만든 파일인 learning_python.txt의 각 줄을 읽고 Python이라는 단어를 C와 같은 다른 언어의 이름으로 바꿉니다. 수정된 각 줄을 화면에 인쇄합니다.
"""

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)
    