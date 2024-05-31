from pathlib import Path    # 라이브러리: 특정 기능을 제공하는 모듈

"""Reading the Contents of a File"""
path = Path('txt/pi_digits.txt')
contents = path.read_text()
# contents = contents.lstrip()
print(contents)


"""Accessing a File's Lines"""
# absolute_file_path = '/Users/sion.noh/widerplanet/repos/test/python-crash-course/chapter10_files_and_exceptions/reading_from_a_file/txt/pi_digits.txt'
# path = Path(absolute_file_path)
# contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line.lstrip())
