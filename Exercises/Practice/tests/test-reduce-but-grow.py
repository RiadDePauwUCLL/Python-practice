import codewars_test as test
from student import grow

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = [
            [6 , [1, 2, 3]],
            [16, [4, 1, 1, 1, 4]],
            [64, [2, 2, 2, 2, 2, 2]],
        ]
        
        for exp, inp in tests:
            test.assert_equals(grow(inp), exp)