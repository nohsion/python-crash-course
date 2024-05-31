from pathlib import Path

"""Writing a Single Line"""
path = Path('txt/programming.txt')
path.write_text("I love programming.")
# path.write_text(12345)  # TypeError: data must be str, not int


"""Writing Multiple Lines"""
# contents = "I love programming.\n"
# contents += "I love creating new games.\n"
# contents += "I love making apps."
#
# # You can also use spaces, tab characters, and blank lines to format your output, just as you’ve been doing with terminal-based output.
# # this is how many computer-generated documents are created.
#
# path = Path('txt/programming.txt')
# path.write_text(contents)