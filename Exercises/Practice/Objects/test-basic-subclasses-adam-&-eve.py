import codewars_test as test
from student import God

paradise = God()
test.assert_equals(isinstance(paradise[0], Man) , True, "First object are a man")