import codewars_test as test
from student import Sphere

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        ball = Sphere(2,50)

        test.assert_approx_equals(ball.get_radius(),2, margin=1e-5, message="Check radius")
        test.assert_approx_equals(ball.get_mass(),50, margin=1e-5, message="Check mass")
        test.assert_approx_equals(ball.get_volume(), 33.51032, margin=1e-5, message="Check volume")
        test.assert_approx_equals(ball.get_surface_area(),50.26548, margin=1e-5, message="Check area")
        test.assert_approx_equals(ball.get_density(),1.49208, margin=1e-5, message="Check density")