block1 = Block([2,2,2])
test.assert_equals(block1.get_width(),2)
test.assert_equals(block1.get_length(),2)
test.assert_equals(block1.get_height(),2)
test.assert_equals(block1.get_volume(),8)
test.assert_equals(block1.get_surface_area(),24)