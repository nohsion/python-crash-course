"""
10-5. Guest Book
사용자에게 이름을 묻는 메시지를 표시하는 프로그램을 작성합니다. (while loop 사용)
사용자가 응답하면 화면에 환영 메시지를 표시하고, 이를 guest_book.txt 파일에 이름을 저장합니다. 사용자가 프로그램을 종료하려면 'q'를 입력하십시오.
"""
from pathlib import Path

path = Path('guest_book.txt')

prompts = "너의 이름이 뭐니? 프로그램을 종료하려면 'q'를 입력하세요.\n"

# 이름 입력받기
names = []
while True:
    name = input(prompts)
    if name == 'q':
        break
    names.append(name)
    print(f"환영합니다, {name} 님!")

# 파일에 입력받은 이름들 저장하기
name_str = ''
for name in names:
    name_str += f"{name}\n"

path.write_text(name_str)
print(f"{path} 파일에 이름들을 저장했습니다.")
