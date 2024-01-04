import codewars_test as test
from student import Python

@test.describe('should pass other tests')
def _():
    @test.it('should support name')
    def name_test():
        bubba = Python('Bubba')
        test.assert_equals(bubba.name, 'Bubba')