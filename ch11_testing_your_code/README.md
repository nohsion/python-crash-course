# Testing Your Code

테스트 코드의 이점

1. 코드가 올바르게 작동할 것이라는 확신을 가질 수 있음 
2. 다른 사람들도 코드가 올바르게 작동할 것이라는 확신을 가질 수 있음
3. 기존 코드의 동작이 깨지지 않는지 확인할 수 있음

pytest 라이브러리 사용
  
- 테스트를 빌드하고, input이 원하는 결과를 나오는지 확인 
- 테스트 통과와 실패 케이스 확인
- 실패한 테스트가 코드를 개선하는 데 어떻게 도움이 되는지 배우게 됩니다.
- 프로젝트에 얼마나 많은 테스트를 작성해야 하는지 이해하게 될 것

## Installing pytest with pip
pip는 파이썬 패키지 관리자. 외부 패키지를 설치하는데 사용됩니다.
보안 문제로, 자주 업데이트 되기 때문에 pip도 업데이트로 시작합니다.
```bash
python -m pip install --upgrade pip
python -m pip install --upgrade package_name
python -m pip install --user pytest
python -m pip install pytest
```
PyCharm IDE에서는 Python Interpreter 설정에서 pytest를 설치할 수 있습니다.

## Testing a Function
직접 프로그램을 실행해서 코드를 테스트할 수 있지만, 테스트를 자동화하면 동작에 대해 항상 확신할 수 있습니다.

### Unit Test (유닛 테스트)
- 가장 대표적인 테스트 유형 중 하나
- 함수 동작이 올바른지 확인
- 테스트 케이스는 단위 테스트의 모음
- 좋은 테스트 케이스는 모든 종류의 input을 고려하고 함수가 예상대로 동작하는지 확인
- full converage를 지닌 테스트케이스는 함수를 사용하는 모든 가능한 방법을 테스트로 커버링한 것
- 대규모 프로젝트에서는 중요 동작에 대해서만 테스트를 작성하는 것이 좋을 때도 있음

### A Passing Test
테스트 파일의 이름과 테스트 함수의 이름은 중요하며, test_로 시작해야 합니다.
pytest는 test_로 시작하는 모든 파일을 찾고, test_로 시작하는 모든 함수를 실행합니다.

```bash
$ pytest
=========================================================================================== test session starts ===========================================================================================
platform darwin -- Python 3.11.1, pytest-8.2.1, pluggy-1.5.0
rootdir: /Users/sion.noh/widerplanet/repos/test/python-crash-course
collected 1 item                                                                                                                                                                                          

ch11_testing_your_code/test_name_function.py .                                                                                                                                                      [100%]

============================================================================================ 1 passed in 0.02s ============================================================================================
```
1. macOS 플랫폼, python 버전, pytest 버전, 이외 패키지 버전
2. 테스트가 실행된 디렉토리
3. 실행된 테스트 파일 수
4. 파일 이름 뒤의 .은 테스트가 성공했음을 의미. 100%는 모든 테스트가 실행되었음을 나타냄
5. 마지막 줄: 테스트 결과 (1개의 테스트 통과, 실행 시간 0.02s 소요)

### A Failing Test
```bash
$ pytest
=========================================================================================== test session starts ===========================================================================================
platform darwin -- Python 3.11.1, pytest-8.2.1, pluggy-1.5.0
rootdir: /Users/sion.noh/widerplanet/repos/test/python-crash-course
collected 2 items                                                                                                                                                                                         

ch11_testing_your_code/test_name_function.py .F                                                                                                                                                     [100%]

================================================================================================ FAILURES =================================================================================================
________________________________________________________________________________________ test_first_last_name_fail ________________________________________________________________________________________

    def test_first_last_name_fail():
>       formatted_name = get_formatted_name_middle('janis', 'joplin')
E       TypeError: get_formatted_name_middle() missing 1 required positional argument: 'last'

ch11_testing_your_code/test_name_function.py:10: TypeError
========================================================================================= short test summary info =========================================================================================
FAILED ch11_testing_your_code/test_name_function.py::test_first_last_name_fail - TypeError: get_formatted_name_middle() missing 1 required positional argument: 'last'
======================================================================================= 1 failed, 1 passed in 0.03s =======================================================================================
```

## Testing a Class

### Commonly Used Assertion Statements in Tests
- assertEqual(a, b): a == b
- assertNotEqual(a, b): a != b
- assertTrue(x): x가 True인지 확인
- assertFalse(x): x가 False인지 확인
- assert element in list: element가 list에 있는지 확인
- assert element not in list: element가 list에 없는지 확인


### Using Fixtures
- 수백, 수천 개의 테스트가 있는 경우, fixture는 테스트 설정에 큰 도움이 된다.
- 데코레이터 @pytest.fixture로 fixture 생성
- 데코레이터는 함수 정의 앞에 배치되는 지시어로, 함수의 동작 방식을 결정한다.
- 지금 같은 경우, 코드가 더 간단해졌다고 보기 어렵지만 테스트가 수만개 있다고 생각해보자. (fixture를 통해 반복을 많이 줄여줌)

## Summary
- pytest 모듈을 통한 function과 class 테스트 작성
- @pytest.fixture로 반복 코드 줄이기
- 테스트 케이스를 잘 짜면, 새로운 작업을 해도 기존 코드가 깨지지 않는 확신을 가질 수 있음
- 버그 발생하는 것보다, 테스트 실패 대응이 훨씬 쉬움
- 다른 프로그래머도 테스트가 있다면 여러분을 더 존중해줄 것. 기꺼이 함께 작업할 것.
- 중요한 로직에 테스트를 작성하되, 특별한 이유가 없다면 full coverage를 목표로 하지 마세요.