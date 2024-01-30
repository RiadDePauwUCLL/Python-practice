import codewars_test as test
from student import Dog


print('Can you make newly created dogs bark?')
apollo = Dog('Apollo', 'Dobermann', 'male', '4')
zeus = Dog('Zeus', 'Dobermann', 'male', '4')

test.assert_equals(apollo.bark(), 'Woof!')
test.assert_equals(zeus.bark(), 'Woof!')