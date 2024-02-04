import codewars_test as test
from student import likes

@test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')