
from forthright_django import forthright_server


# test1 -- mixed type input arguments and multiple outputs
def calculate_values(operation, x, y, z):
    if operation == 'add':
        result1 = x + y
        result2 = y + z
    elif operation == 'multiply':
        result1 = x * y
        result2 = y * z
    else:
        result1 = x
        result2 = y

    return result1, result2


# test2 -- kwargs input with single output
def concat_words(word1, word2, word3):
    combine = word1 + word2 + word3
    return combine


# test3 -- input and output are a custom object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def increment_age(person):
    person.age += 1
    return person


# test4 -- zero input arguments
def optional_input(optional_arg=42):
    return optional_arg


# test5 -- argument is an arbitrary type
def send_back_same(arg):
    return arg



frs = forthright_server(safe_mode=False)
frs.export_functions(calculate_values, concat_words, increment_age, optional_input, send_back_same)


