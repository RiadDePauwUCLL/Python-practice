import codewars_test as test

# for backward compatibility
try:
    from student import findSmallestInt as find_smallest_int
except ImportError:
    from student import find_smallest_int

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
        test.assert_equals(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
        test.assert_equals(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)