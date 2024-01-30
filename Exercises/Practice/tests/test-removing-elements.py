import codewars_test as test
from student import remove_every_other

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
                        ['Hello', 'Hello Again'])
        test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                        [1, 3, 5, 7, 9])
        test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
        test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
                        [['Goodbye']])
