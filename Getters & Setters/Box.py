class Box:
    def __init__(self, contents):
        self.contents = contents

    # This is the getter
    @property
    def contents(self):
        print('Reading')
        return self.__contents
    
    # This is the setter
    @contents.setter
    def contents(self, value):
        print('Writing')
        self.__contents = value

box = Box(5)
print(box.contents)
# Writing = Because constructor sets property
# Reading = Because property's getter was called
#       5 = Property returned 5   