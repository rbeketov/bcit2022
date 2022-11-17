from gen_random import gen_random

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
