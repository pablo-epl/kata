import codewars_test as test

"""
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
"""

def next_bigger(number):
    number = list(str(number)[::-1])
    index = 0
    index_splitter = None
    while index < len(number)-1 and not index_splitter:
        if number[index] > number[index+1]:
            index_splitter = index+1
        index += 1
    if not index_splitter:
        return -1

    number_left_part = number[:index_splitter]
    number_right_part = number[index_splitter+1:]
    middle_number = number[index_splitter]
    number_left_part = sorted(number_left_part)

    for index in enumerate(number_left_part):
        if number_left_part[index] > middle_number:
            replaced_number = number_left_part[index]
            number_left_part[index] = middle_number
            middle_number = replaced_number
            break

    result = sorted(number_left_part, reverse=True)
    result.append(middle_number)
    result.extend(number_right_part)
    result = result[::-1]
    return int(''.join(result))

@test.it('Test Cases')
def example_test_case():
    test.assert_equals(next_bigger(12), 21)
    test.assert_equals(next_bigger(513), 531)
    test.assert_equals(next_bigger(2017), 2071)
    test.assert_equals(next_bigger(414), 441)
    test.assert_equals(next_bigger(144), 414)
    test.assert_equals(next_bigger(26067758652), 26067762558)
    test.assert_equals(next_bigger(531), -1)
    test.assert_equals(next_bigger(111), -1)
    test.assert_equals(next_bigger(9), -1)
