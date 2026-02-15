import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from calculator.price import apply_discount, add_vat

#Link feature file
scenarios("features/price.feature")

@pytest.fixture
def context():
    return {}

@given(parsers.parse("the original price is {price:d}"))
def original_price(context, price):
    context["price"] = price

@when(parsers.parse("I apply a discount of {discount:d} percent"))
def apply_discount_step(context, discount):
    context["result"] = apply_discount(context["price"], discount)

@when(parsers.parse("I add VAT of {vat:d} percent"))
def add_vat_step(context, vat):
    context["result"] = add_vat(context["price"], vat)

@then(parsers.parse("the final price should be {expected: d}"))
def check_result(context, expected):
    assert context["result"] == expected    