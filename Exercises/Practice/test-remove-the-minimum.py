import codewars_test as test
from student import remove_smallest
from numpy.random import randint

def randlist():
    return list(randint(400, size=randint(1, 10)))

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
        test.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
        test.assert_equals(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
        test.assert_equals(remove_smallest([]), [], "Wrong result for []")
        
    @test.it("check for mutations to original list")    
    def _():
        a = randlist() # generates the list
        b = list(a) # makes a swallow copy
        remove_smallest(a) # uses the original list with the function
        test.assert_equals(a, b, "You've mutated input list  (expectation assertion is on value of input list, not output of method)") # test the list match