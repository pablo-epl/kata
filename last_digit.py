import codewars_test as test

'''
Define a function that takes in two non-negative integers a and b and returns
the last decimal digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969.
The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits,
is 6. Also, please take 0^0 to be 1.

You may assume that the input will always be valid.

Examples
```
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
```

'''
def last_digit(n1, n2):
    n1_last_digit = None
    if n1 < 1 or n2 < 1:
        n1_last_digit = 1
    if not n1_last_digit and n1 > 0 and n2 > 0:
        n1_last_digit = int(str(n1)[-1])
        if n1_last_digit in [4, 9]:
            n2_mod = n2%2
            n2_mod = 1 if n2_mod != 0 else 2
            n1_last_digit = n1_last_digit ** n2_mod
            n1_last_digit = int(str(n1_last_digit)[-1])
        elif n1_last_digit in [2, 3, 7, 8]:
            n2_mod = n2%4
            n2_mod = 4 if n2_mod == 0 else n2_mod
            n1_last_digit = n1_last_digit**n2_mod
            n1_last_digit = int(str(n1_last_digit)[-1])
    return n1_last_digit

@test.it('Test Cases')
def example_test_case():
    test.assert_equals(last_digit(4, 1), 4)
    test.assert_equals(last_digit(4, 2), 6)
    test.assert_equals(last_digit(4, 3), 4)
    test.assert_equals(last_digit(4, 4), 6)
    test.assert_equals(last_digit(4, 5), 4)
    test.assert_equals(last_digit(9, 7), 9)
    test.assert_equals(last_digit(10, 10 ** 10), 0)
    test.assert_equals(last_digit(2 ** 200, 2 ** 300), 6)
    test.assert_equals(last_digit(7, 1), 7)
    test.assert_equals(last_digit(7, 2), 9)
    test.assert_equals(last_digit(7, 3), 3)
    test.assert_equals(last_digit(7, 4), 1)
    test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)
    test.assert_equals(last_digit(698599406124379437753367290461810933720146221699284327007, 5751577441191891781287111760536750515540625810366212823872), 1)
    test.assert_equals(last_digit(538075703718845089730956746855479065310731046980147700642, 19633868178283970565574000644639271911782901409503594680308), 6)
    test.assert_equals(last_digit(340445841487427019441537477208354516915950224255514095398, 2461861269304745114415664820196221808962378424966127865176), 6)

@test.it("x ** 0")
def second_example_test_case():
    for nmbr in range(1, 9):
        a = nmbr ** nmbr
        test.it("Testing %d and %d" % (a, 0))
        test.assert_equals(last_digit(a, 0), 1, "x ** 0 must return 1")
887ms