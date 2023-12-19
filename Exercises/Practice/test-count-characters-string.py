import codewars_test as test
from student import count

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(count('aba'), {'a': 2, 'b': 1})
        test.assert_equals(count(''), {})
        test.assert_equals(count('aa'), {'a' : 2})
        test.assert_equals(count('aabb'), {'b' : 2, 'a' : 2})