# ch10. Files And Exceptions
- Files: 많은 데이터를 빠르게 분석할 수 있도록 File로 작업하는 것을 배웁니다.
- Exceptions: 예기치 않은 상황에 프로그램이 종료되지 않도록 예외를 처리하는 방법을 배웁니다. 실수든 악의적인 시도이든 간에 견고한 프로그램을 짤 수 있습니다. 
- json 모듈 사용법


## 1. Files

### 문자열 합치기 방법 (line별로 읽어서 합칠때)
```python
# 1. += 연산자 사용
str1 = 'Hello '
str1 += 'World '
str1 += 'Python'
print(f"str1: {str1}")

# 2. join() 메소드 사용
str2 = ' '.join(['Hello', 'World', 'Python'])
print(f"str2: {str2}")

# 3. f-string 사용
a1, a2, a3 = 'Hello', 'World', 'Python'
str3 = f'{a1} {a2} {a3}'
print(f"str3: {str3}")
```

## 2. Exceptions

파이썬은 예외라는 특수 객체를 사용하여 프로그램 실행 중에 발생하는 오류를 관리합니다.
- 예외 처리 O: 프로그램이 계속 실행됨
- 예외 처리 X: 프로그램이 중지되고 traceback이 표시됨
예외는 try-except 블록으로 처리됩니다.
try-except 블록은 파이썬에 어떤 작업을 요청하지만, 예외가 발생하면 어떻게 해야 하는지 파이썬에 알려주기도 합니다.
사용자가 읽기에 혼란스러울 수 있는 traceback 대신 개발자가 작성한 친숙한 오류 메시지가 표시됩니다.

### Handling the ZeroDivisionError Exception
`division_calculator.py` 예시 확인

### The else Block
`division_calculator.py` 예시 확인
- 파일을 읽을 때, 파일이 존재하지 않으면 FileNotFoundError가 발생합니다.
- 이때, try-except 블록을 사용하여 파일이 존재하지 않을 때의 예외를 처리할 수 있습니다.
- try 블록이 성공적으로 실행되면 else 블록이 실행됩니다.

### Deciding Which Errors to Report
사용자에게 오류를 알려줄 지, 조용히 넘어가도록(pass) 할 지를 어떻게 정할까요?
- 사용자가 오류를 이해할 수 있는 경우: 오류 메시지 표시
- 사용자가 오류를 이해할 수 없는 경우: 조용히 넘어가도록
- 잘 작성되고 테스트된 코드는 구문이나 논리적 오류와 같은 내부 오류가 잘 발생하지 않습니다.
- 하지만 user input, file 존재여부, network connection 등 외부 요인에 의해 발생하는 오류는 예상할 수 없습니다.
- 결국에 경험을 통해 try-except 블록을 잘 사용할 수 있을 것입니다.


## Storing Data
json 모듈로 데이터를 저장해봅시다.
python 뿐 아니라 다른 언어에서도 json 형식을 사용하여 데이터를 저장하고 전송합니다.
- JSON(JavaScript Object Notation): 원래 자바스크립트용으로 개발되었으나, 일반적인 포맷으로 사용되는 중
- json.dumps(): 파이썬 객체를 JSON 형식으로 변환
- json.loads(): JSON 형식의 문자열을 파이썬 객체로 변환