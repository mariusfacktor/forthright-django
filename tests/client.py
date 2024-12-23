
from forthright_django import forthright_client


url = 'http://127.0.0.1:8000'

frc = forthright_client(url)
frc.import_functions('calculate_values', 'concat_words', 'increment_age', 'optional_input', 'input_list')


# test1 -- mixed type input arguments and multiple outputs
val1, val2 = frc.calculate_values('add', 2, 3, 4)
print('%d %d' %(val1, val2)) # -> 5 7


# test2 -- kwargs input with single output
concat_output = frc.concat_words(word1='aaa', word2='bbb', word3='ccc')
print(concat_output) # -> aaabbbccc


# test3 -- input and output are a custom object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('john', 38)
older_person = frc.increment_age(p1)
print(older_person.age) # -> 39


# test4 -- zero input arguments
default_val = frc.optional_input()
print(default_val) # -> 42


# test5 -- argument is a list 
output_list = frc.input_list(['this', 'is', 'a', 'list'])
print(output_list) # -> ['this', 'is', 'a', 'list']


