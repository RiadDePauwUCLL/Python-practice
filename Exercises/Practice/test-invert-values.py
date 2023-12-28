import codewars_test as test
from student import invert

@test.describe("Invert values")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
        test.assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
        test.assert_equals(invert([]), [])