def raise_stop_iteration():
    my_iterator = iter([1, 2, 3])
    for i in range(4):
        next(my_iterator)

def raise_zero_division_error():
    x = 1 / 0

def raise_assertion_error():
    x = 10
    y = 20
    assert x > y, "x is not greater than y"

'''def raise_import_error():
    import non_existent_module'''

def raise_key_error():
    my_dict = {"key": "value"}
    value = my_dict["non_existent_key"]

'''def raise_syntax_error():
    if True
        print("Hello")'''

'''def raise_indentation_error():
    def my_function():
    print("This line is not properly indented")'''

def raise_type_error():
    x = "hello"
    result = x + 42


#raise_stop_iteration()
#raise_zero_division_error()
#raise_assertion_error()
#raise_import_error()
#raise_key_error()
#raise_syntax_error()
#raise_indentation_error()
raise_type_error()