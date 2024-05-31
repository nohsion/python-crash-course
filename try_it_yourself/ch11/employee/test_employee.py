import pytest

from employee import Employee


def test_give_default_raise():
    employee = Employee('sion', 'noh', 50_000)
    employee.give_raise()
    assert employee.salary == 55_000


def test_give_custom_raise():
    employee = Employee('sion', 'noh', 50_000)
    employee.give_raise(100_000)
    assert employee.salary == 150_000


@pytest.fixture
def employee():
    return Employee('sion', 'noh', 50_000)


def test_give_default_raise_using_fixture(employee):
    employee.give_raise()
    assert employee.salary == 55_000


def test_give_custom_raise_using_fixture(employee):
    employee.give_raise(100_000)
    assert employee.salary == 150_000
