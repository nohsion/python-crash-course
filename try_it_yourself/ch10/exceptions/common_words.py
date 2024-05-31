"""
10-10. Common Words
count() 메서드를 사용하여 문자열에 특정 단어가 몇 번 나타나는지 계산하는 프로그램을 작성하세요.
"""

from pathlib import Path


def count_common_words(filename, word):
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"죄송합니다. '{filename}' 파일을 찾을 수 없습니다.")
        return
    word_cnt = contents.lower().count(word)
    print(f"'{word}' 단어는 파일 '{filename.split('/')[-1]}'에 {word_cnt}번 나타납니다.")


filename = '../../../ch10_files_and_exceptions/exceptions/txt/alice.txt'
count_common_words(filename, 'the')
