"""Handling the ZeroDivisionError Exception"""
# print(5/0)  # ZeroDivisionError: division by zero


"""Using try-except Blocks"""
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")


"""Using Exceptions to Prevent Crashes"""
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)


"""The else Block"""
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:  # else 블록은 try 블록이 성공적으로 실행되었을 때 실행됨
#         print(answer)