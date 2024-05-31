"""
10-6. Addition
숫자 입력을 요청할 때 흔히 발생하는 문제 중 하나는 사용자가 숫자 대신 텍스트를 입력할 때 발생합니다.
입력을 정수로 변환하려고 하면 ValueError가 발생합니다. 두 개의 숫자를 입력하라는 메시지를 표시하는 프로그램을 작성해 보세요.
두 숫자를 더하고 결과를 인쇄합니다. 입력값 중 하나가 숫자가 아닌 경우 ValueError를 발생시키고 알기 쉬운 오류 메시지를 출력합니다.
두 개의 숫자를 입력한 다음 숫자 대신 텍스트를 입력하여 프로그램을 테스트해 보세요.
"""


def add_two_numbers():
    try:
        first_number = int(input("첫번째 숫자를 입력하세요: "))
        second_number = int(input("두번째 숫자를 입력하세요: "))
    except ValueError:
        print("숫자를 입력하라고 했죠!!")
    else:
        result = first_number + second_number
        print(f"결과: {first_number}+{second_number}={result}")


add_two_numbers()
