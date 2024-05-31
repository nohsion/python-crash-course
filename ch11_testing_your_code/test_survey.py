import pytest
from survey import AnonymousSurvey


def test_store_single_response():
    # 응답 하나 저장. 그런데 설문조사는 최소 3개 이상은 되어야지.
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    my_survey.store_response('English')
    assert 'English' in my_survey.responses


def test_store_three_responses():
    # 응답 세 개 저장. 그러나 다소 중복되고 반복적인 작업이라, pytest의 다른 기능을 사용해서 더 효율적으로 짜보자.
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        my_survey.store_response(response)

    for response in responses:
        assert response in my_survey.responses


@pytest.fixture
def language_survey():
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)


def test_store_single_response_using_fixture(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_responses_using_fixture(language_survey):
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
