from radish import given, when, then, custom_type, register_custom_type, TypeBuilder
import os
import sys
sys.path.append(os.getcwd())
from unique import Unique

@custom_type('Number', r'\d*')
def parse_number(text):
    if text.isdigit():
        return int(text)
    elif text == "None":
        return None
    return text

# register the NumberList type
register_custom_type(NumberList=TypeBuilder.with_many0(
    parse_number, listsep=','))

@given("the list {test_list:NumberList}")
def have_list(step, test_list):
    step.context.test_list = test_list

@when("Unique them")
def unique_them(step):
    step.context.result = list(Unique(step.context.test_list))

@then("result to be {result:NumberList}")
def expect_result(step, result):
    assert step.context.result == result
