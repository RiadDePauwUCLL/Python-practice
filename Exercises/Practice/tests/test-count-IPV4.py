import codewars_test as test
from student import ips_between

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(ips_between("10.0.0.0", "10.0.0.50"), 50)
        test.assert_equals(ips_between("20.0.0.10", "20.0.1.0"), 246)

