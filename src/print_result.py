def print_result(func_to_decorate):

    def decoreate_func(*args, **kwargs):
        print(func_to_decorate.__name__)
        data = func_to_decorate(*args, **kwargs)
        if type(data) == list:
            for _ in data:
                print(_)
        elif type(data) == dict:
            for _ in data:
                key = data[_]
                print(f"{_} = {key}")
        else:
            print(data)
        return data
    return decoreate_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
