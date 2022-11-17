import json
import sys

from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique
from print_result import print_result
# Сделаем другие необходимые импорты

path = "data_light.json"

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк


@print_result
def sort_unique(data_arg):
    return sorted([it for it in Unique([i["job-name"] for i in data_arg], bool_ignore_case = True)])

@print_result
def check_start(data_arg):
    return [it.title() for it in list(filter(lambda x: x.startswith("программист"), data_arg))]


@print_result
def add_lit(data_arg):
    return list(map(lambda x: x + " с опытом Python", data_arg))


@print_result
def add_salary(data_arg):
    return list(zip(data_arg, gen_random(len(data_arg), 100000, 200000)))

if __name__ == '__main__':
    with cm_timer_1():
        add_salary(add_lit(check_start(sort_unique(data))))