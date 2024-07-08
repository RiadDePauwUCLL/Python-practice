import codewars_test as test

try:
    from student import dirReduc as dir_reduc
except ImportError:
    from student import dir_reduc

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        test.assert_equals(dir_reduc(a), ['WEST'])
        a=["NORTH", "WEST", "SOUTH", "EAST"]
        test.assert_equals(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] # ['WEST']
        test.assert_equals(dir_reduc(a), ['WEST'])
        a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"] # ['NORTH', 'NORTH']
        test.assert_equals(dir_reduc(a), ['NORTH', 'NORTH'])
        a = [] # []
        test.assert_equals(dir_reduc(a), []) 
        a=["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"] # []
        test.assert_equals(dir_reduc(a), [])
        a = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"] # ["NORTH"]
        test.assert_equals(dir_reduc(a), ["NORTH"])
        a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"] # ["EAST", "NORTH"]
        test.assert_equals(dir_reduc(a), ["EAST", "NORTH"])
        a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"] # ["NORTH", "EAST"])
        test.assert_equals(dir_reduc(a), ["NORTH", "EAST"])
        a = ["NORTH", "WEST", "SOUTH", "EAST"] # ["NORTH", "WEST", "SOUTH", "EAST"])
        test.assert_equals(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
        a = ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
        test.assert_equals(dir_reduc(a), ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])        