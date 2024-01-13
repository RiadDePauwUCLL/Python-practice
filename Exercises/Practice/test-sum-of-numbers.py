from student import get_sum
import codewars_test as test


@test.describe('Sum of numbers')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(get_sum(0,1),1)
        test.assert_equals(get_sum(0,-1),-1)