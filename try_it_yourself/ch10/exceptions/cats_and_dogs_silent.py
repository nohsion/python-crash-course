"""
10-9. Silent Cats and Dogs
10-8의 프로그램을 수정하여 FileNotFoundError가 발생했을 때 프로그램이 조용히 종료되도록 만들어 보세요.
"""

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        continue
    print(contents)
