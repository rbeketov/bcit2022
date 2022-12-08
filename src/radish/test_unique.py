from radish import given, when, then, custom_type, register_custom_type, TypeBuilder

# import sys
# sys.path.append('../')
# from unique import Unique

class Unique:
    def __init__(self, data, **kwargs):
        self.used_elements = set() 
        self.data = data
        self.index = 0
        if len(kwargs) == 0:
            self.bool_ignore_case = False
        else:
            self.bool_ignore_case = kwargs["bool_ignore_case"]
        self.tmp_list = [i for i in self.data]

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.tmp_list):
                raise StopIteration
            else:
                current = self.tmp_list[self.index]
                if (type(current) == str and self.bool_ignore_case):
                    current = current.lower()
                self.index = self.index + 1
                if current not in self.used_elements:
                    self.used_elements.add(current)
                    return current



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