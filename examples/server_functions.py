from forthright_django import forthright_server

def add_and_sub(numA, numB):
    return numA + numB, numA - numB

frs = forthright_server()
frs.export_functions(add_and_sub)


