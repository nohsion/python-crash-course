from pathlib import Path

absolute_file_path = '/Users/sion.noh/widerplanet/repos/test/python-crash-course/ch10_files_and_exceptions/reading_from_a_file/txt/pi_digits.txt'
path = Path(absolute_file_path)
contents = path.read_text()

lines = contents.splitlines()
for line in contents.splitlines():
    print(line.lstrip())
