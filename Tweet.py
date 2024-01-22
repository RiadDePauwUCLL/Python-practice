# My explanation of the Tweet assignment.

# Before starting:
# 0. The explanation is based on the assignment Tweet from chapter Objects.
# 1. I may understand some things wrongly or not profoundly!
# 2. Remember that property with name 'test' is ran only if field self.test is accessed. If we access self.__test, property 'test' will not be ran.
# 3. Private fields don't exists as a feature of Python language. All fields are public. Prepending a field's name with double underscore is merely a convention that programmers use to help them and their teammates differentiate between which field should be accessed directly and which indirectly, e.g. through a property or a method of somekind.

# We start with creating a class Tweet that has two private fields in the constructor. These two fields can be initialized when instantiating the class.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.__max_length = max_length

# We add a public property named message that gives us access to private field message. Note that this means that the property will be ran only if we call self.message. Because the name of the property is message, not __message. If we call self.__message, Python will just read the field self.__message from the constructor without using the property.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.__max_length = max_length
    
    @property
    def message(self):
        return self.__message

# The message setter must guard against oversized tweets, thus it truncates the new message to the length max_length.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.__max_length = max_length
    
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, new_message):
        self.__message = new_message[:self.__max_length]

# Let's test. We make a breakpoint on the line of instantiation and press F5 to start debugging. We see that the code effectively skips our message setter. This is because our property is named 'message', thus it targets the field self.message. But that field never gets set; we're using self.__message field insead. So let's change that and make our public property useful.
tweet = Tweet("hello", 3)
print('hel', tweet.message)

# We changed private field message to public field. If we debug again, we see that the setter code starts executing. The new_message gets a value 'hello', but when the setter tries to truncate it, we get an error "'Tweet' object has no attribute '_Tweet__max_length'". This is because the code execution has not yet initialized self.__max_length field. Remember, the code was still in the process of setting the self.message field, it hasn't gotten to the second field.
# Though each new message has to get truncated immediately. What are the options?
class Tweet:
    def __init__(self, message, max_length):
        self.message = message
        self.__max_length = max_length
    
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, new_message):
        self.__message = new_message[:self.__max_length]

# If we rethink the situation a bit: We will have to truncate the message in two scenarios. Firstly, if new message is set, secondly, if __max_length is changed. To truncate a messsage, we need both the message and the maximum length. But our code sees only self.message. What if we skip truncating only for the first time (at instantiation) and only in the message setter? We can skip (not call) the message setter if we change the self.message to self.__message as we had in the beginning.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.__max_length = max_length
    
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, new_message):
        self.__message = new_message[:self.__max_length]    

# Let's now create the second public property named max_length, as said in the instruction.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.__max_length = max_length
    
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, new_message):
        self.__message = new_message[:self.__max_length] # Truncating.
    
    @property
    def max_length(self):
        return self.__max_length
    @max_length.setter
    def max_length(self, new_max_length):
        self.__max_length = new_max_length
        self.__message = self.__message[:self.__max_length] # Truncating.

# max_length getter returns the private field __max_length, that's OK. max_length setter sets the private field __max_length to new value and starts to truncate the message. If we debug with the same two lines as before, we see that it does not succeed. This is because max_length setter is never called. And same is with message setter. max_length setter will be called, when we try to assign a value to a field named exactly max_length (self.max_length). But we never assing anything to a field self.max_length. And our goal is actually that when code execution comes to self.__max_length = max_length, the max_length setter gets called and truncates the message. The solution is simple, by changing self.__max_length to self.max_length in the constructor, the max_length setter will be called.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.max_length = max_length
    
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, new_message):
        self.__message = new_message[:self.__max_length] # Truncating.
    
    @property
    def max_length(self):
        return self.__max_length
    @max_length.setter
    def max_length(self, new_max_length):
        self.__max_length = new_max_length
        self.__message = self.__message[:self.__max_length] # Truncating.

# Note that by changing max_length from private to public, our max_length setter now CREATES a new private field self.__max_length. And from now on, our class code only uses __max_length. Our code finnaly works. But let's make some redundancy clear by changing message setter.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.max_length = max_length
    
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, new_message):
        self.__message = new_message
        self.__message = self.__message[:self.__max_length] # Truncating.
    
    @property
    def max_length(self):
        return self.__max_length
    @max_length.setter
    def max_length(self, new_max_length):
        self.__max_length = new_max_length
        self.__message = self.__message[:self.__max_length] # Truncating.
# We can now clearly see that both setter have same truncate code. It's always nice to pack it into a function or method in this case. Let's name it 'truncate'. And because this piece of code only operates with private fields, we want to indicate that by changing the name of the method to '__truncate', thus making it recognizable as a private method.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.max_length = max_length
    
    def __truncate(self):
        self.__message = self.__message[:self.__max_length]

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, new_message):
        self.__message = new_message
        self.__truncate()
    
    @property
    def max_length(self):
        return self.__max_length
    @max_length.setter
    def max_length(self, new_max_length):
        self.__max_length = new_max_length
        self.__truncate()

# The code still doesn't pass pytest and that's because I didn't remember to add an obvious condition explicitly specified in the assignment. Maximum length must be at least 1.
class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.max_length = max_length
    
    def __truncate(self):
        self.__message = self.__message[:self.__max_length]

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, new_message):
        self.__message = new_message
        self.__truncate()
    
    @property
    def max_length(self):
        return self.__max_length
    @max_length.setter
    def max_length(self, new_max_length):
        if new_max_length < 1:
            raise ValueError()
        self.__max_length = new_max_length
        self.__truncate()

