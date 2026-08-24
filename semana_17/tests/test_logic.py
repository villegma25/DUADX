import pytest
from my_module.logic import FinanceManager


def test_add_category_success():
    ...


def test_add_category_empty_name_raises():
    ...


def test_add_category_duplicate_raises():
    ...


def test_add_movement_without_categories_raises():
    ...


def test_add_movement_category_does_not_exist_raises():
    ...


def test_add_movement_amount_must_be_positive_raises():
    ...


def test_add_expense_stored_as_negative():
    ...


def test_add_income_stored_as_positive():
    ...


def test_total_balance_correct():
    ...


def test_total_income_and_expense():
    ...