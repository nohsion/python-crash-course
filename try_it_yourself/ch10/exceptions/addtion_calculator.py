"""
10-7. Addtion Calculator
이전에 만든 add_two_numbers() 함수에 while 루프를 추가하여 사용자가 프로그램을 끝내길 원할 때까지 계속해서 두 숫자를 더할 수 있게 만들어 보세요.
"""

print("프로그램을 종료하려면 언제든 'q'를 입력하세요.")

while True:
    try:
        first_input = input("첫번째 숫자를 입력하세요: ")
        if first_input == 'q':
            break
        first_number = int(first_input)
        second_input = input("두번째 숫자를 입력하세요: ")
        if second_input == 'q':
            break
        second_number = int(second_input)
        result = first_number + second_number
    except ValueError:
        print("숫자를 입력하라고 했죠!!")
    else:
        print(f"결과: {first_number}+{second_number}={result}")