import codewars_test as test
from student import rental_car_cost

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(rental_car_cost(1),40)
        test.assert_equals(rental_car_cost(4),140)
        test.assert_equals(rental_car_cost(7),230)
        test.assert_equals(rental_car_cost(8),270)
