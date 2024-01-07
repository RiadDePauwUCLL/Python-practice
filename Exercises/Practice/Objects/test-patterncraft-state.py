@test.describe('Basic tests')
def __():
    @test.it('Tank State')
    def _():
        tank = Tank()
        test.assert_equals(tank.can_move(), True)
        test.assert_equals(tank.damage(), 5)
    
    @test.it('Siege State')
    def _():
        tank = Tank()
        tank.state = SiegeState()
        test.assert_equals(tank.can_move(), False)
        test.assert_equals(tank.damage(), 20)
    
    @test.it('Mix State')
    def _():
        tank = Tank()
        test.assert_equals(tank.can_move(), True)
        tank.state = SiegeState()
        test.assert_equals(tank.damage(), 20)