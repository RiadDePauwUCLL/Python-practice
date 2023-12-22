import codewars_test as test
from student import rps

@test.describe("rock paper scissors")
def basic_tests():
    @test.it("Player 1 wins")
    def player_1():
        test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
    @test.it("Player 1 wins")
    def player_1():
        test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
    @test.it("Draw")
    def draw():
        test.assert_equals(rps('rock', 'rock'), 'Draw!')
    
