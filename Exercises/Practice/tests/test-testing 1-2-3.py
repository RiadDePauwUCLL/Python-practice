import codewars_test as test
from student import number

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(number([]), [])
        test.assert_equals(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])