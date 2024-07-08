import codewars_test as test
from student import calculate_years

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(calculate_years(1000, 0.05, 0.18, 1100), 3)
        test.assert_equals(calculate_years(1000,0.01625,0.18,1200), 14)
        test.assert_equals(calculate_years(1000,0.05,0.18,1000), 0)