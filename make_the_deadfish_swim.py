import codewars_test as test

"""
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
"""

def parse(data):
    dead_fish_result = []
    dead_fish_value = 0
    for command in data:
        if command == 'i':
            dead_fish_value += 1
        elif command == 'd':
            dead_fish_value -= 1
        elif command == 's':
            dead_fish_value *= dead_fish_value
        elif command == 'o':
            dead_fish_result.append(dead_fish_value)
    return dead_fish_result

@test.it('Test Cases')
def example_test_case():
    test.assert_equals(parse("ooo"), [0, 0, 0])
    test.assert_equals(parse("ioioio"), [1, 2, 3])
    test.assert_equals(parse("idoiido"), [0, 1])
    test.assert_equals(parse("isoisoiso"), [1, 4, 25])
    test.assert_equals(parse("codewars"), [0])