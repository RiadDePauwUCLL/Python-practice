import codewars_test as test
from student import test_solution_main

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Testing with no extra parameter")
    def basic_test_cases():
        #the preloaded testing functions calls the function and compares what
        #it prints with the result parameter
        test_solution_main(Solution.main,result="Hello World!")
    @test.it("Testing with 'Hola mundo!' as extra parameter")
    def basic_test_cases():
        test_solution_main(Solution.main,["Hola mundo!"],result="Hello World!")