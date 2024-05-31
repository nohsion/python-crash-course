from pathlib import Path


"""Working with a File's Contents"""
path = Path('txt/pi_million_digits.txt')  # https://www.piday.org/million/
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
