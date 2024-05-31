"""
10-1. Learning Python
텍스트 편집기에서 빈 파일을 열고 지금까지 파이썬에 대해 배운 내용을 요약하여 몇 줄로 작성합니다.
각 줄은 "In Python you can..." 이 파일을 이 장에서 연습한 것과 같은 디렉터리에 learning_python.txt로 저장합니다.
파일을 읽고 작성한 내용을 두 번 인쇄하는 프로그램을 작성합니다.
한 번은 파일 전체를 읽어 내용을 인쇄하고, 한 번은 줄을 목록에 저장한 다음 각 줄을 반복하여 내용을 인쇄합니다.
"""


from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)  # 전체 내용 출력

print("------")
lines = contents.splitlines()
for line in lines:
    print(line)
