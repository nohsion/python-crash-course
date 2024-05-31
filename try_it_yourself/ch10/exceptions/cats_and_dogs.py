"""
10-8. Cats and Dogs
cats.txt와 dogs.txt 두 파일을 만드세요.
cats.txt에는 고양이 이름을 3개 이상, dogs.txt에는 강아지 이름을 3개 이상 적으세요.
FileNotFound 예외 잡아서 메시지도 남기세요. 다른 path로 옮겨서 예외 코드가 실행되는지 테스트해보세요.
"""

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"죄송합니다. '{filename}' 파일을 찾을 수 없습니다.")
        continue  # else 대신 사용해 봄
    print(contents)
