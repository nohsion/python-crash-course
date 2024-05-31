from pathlib import Path


"""Working with a File's Contents"""
path = Path('txt/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line
    # pi_string += line.lstrip()


print(pi_string)
print(len(pi_string))
