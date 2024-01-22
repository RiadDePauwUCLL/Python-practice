# Make sure you have all the names correct
# this includes function, class, method, and parameters



#Question 1

def csom(n):
   n_str = str(n)
   sum_of_digits = sum(int(digit) for digit in n_str)
   if sum_of_digits < 10:
       return sum_of_digits
   else:
       return csom(sum_of_digits)
   

#Question 2

def isPalindrome(t):
   return t == t[::-1]


#Question 3
class Attraction: #Define our Class
    
    def __init__(self , name, height): #Create a constructor with a which takes 3 parameters self (a reference to the instance being initialized), name (the name of the attraction), and height (the minimum height requirement for riders).
        self.name = name  #It initializes the name as the name paramter we give it.
        self.height = height #It initializes the height as the height paraeter we give it.
        self.visitors = 0 # It initializes the visitors attribute to 0.

    @property #Here we define our getter.
    def name(self) -> str: 
        return self.__name #this method simply returns the value of the name attribute from the init.
        
    @name.setter
    def name(self, val):
        if type(val) is not str or len(val) == 0: #This checks if the value is not a string and empty.
            raise ValueError("Lmao you made an oopsie daisy") #A vlaue error is raised if so.
        self.__name = val #Otherwise the name is set to the value.

    def visit(self, height): #Here a method is defined.
       min_height = 100 #We give it 2 varriables it will use for a condition.
       max_height = 200
       if min_height <= height <= max_height: #If this condition returns true then...
           self.visitors += 1 #1 is added to the visitor count.
       else: #Otherwise...
           with open('log.txt', 'a') as f: #A log text file is opened as f, 'a' appends to the end of the file.
               f.write(f"Visitor with height {height} cm was not allowed.\n") #We write to the file the given height of the visitor and some accompanying text.

#Here we have 3 instances of the Attraction Class being created as 3 objects (aka different attractions):
pagode = Attraction("De Pagode", 0)
max_moritz = Attraction("Max & Moritz", 100)
baron = Attraction("De Baron", 132)
#As you can see each are stored in their won "variable of sorts" then you write the name of the class and fill in values the constructor needs to take (the name and height.)

#Here we have 2 instances of visitors attempting to go on a ride in max_moritz so we call the visit method on max_moritz and give the height parameter it looks for!
max_moritz.visit(105) 
max_moritz.visit(110)


#Question 4

class ThemePark: #Define our Class Theme Park.
   
    def __init__(self, name): #Create our constructor which take a name parameter.
       self._name = name 
       self.attractions = [] #We also give attractions and initial value of an empty list.

    @property #Here we define our getter.
    def name(self):
       return self._name #This method simply returns the name.

    @name.setter #Here we define our setter.
    def name(self, value): 
       if not value: #We check if the value is empty.
           raise ValueError("Name cannot be empty") #if it is a value error is raised stating so.
       elif not value[0].isupper(): #We then check if the first letter of the inputted name is capital or not.
           raise ValueError("Name has to start with a capital letter") #if it isn't a value error is raised stating so.
       else:
           self._name = value #In any other case it returns the name as value.

    def addAttraction(self, attraction): #We define a method to add Attractions here looking for a parameter attraction.
       normalized_name = attraction.name.lower().replace(' ', '') #To avoid issues we normalize the name by forcing all the characters to lowercase and by replacing all spaces with no spaces.
       if not any(a.name.lower().replace(' ', '') == normalized_name for a in self.attractions): #Here we check if there is any existing attraction in self.attractions whose name matches the normalized name of the attraction being added.
           self.attractions.append(attraction) #If not we append it to attraction.

    def printOverview(self): #Here we define a math to print an overview of the attraction.
       total_visits = sum(a.visits for a in self.attractions) #sotres all visits of an attraction by summing them up.
       print(f"{self.name} is an amusement park with {len(self.attractions)} attractions visited a total of {total_visits} times.") #prints the information.



    def securityUpdate(self, filename): #here we define the security update parameter and it looks for a filename parameter.
        with open(filename, 'r') as file: #We open our inputted file as file and only read from it 'r'.
            for line in file: #For every line in the file...
                height, attractions = line.strip().split(': ') #Removes leading and trailing whitespaces from a string and splits (using delimiter ': ') them and stores them into 2 separate variables.
                height = int(height[:-3]) # remove cm from the end of height & the space. Much more simplistic
                attractions = attractions.split(', ') #Splits the attractions using the delimiter (', ')

                for attraction in attractions: #For every attraction in our attractions list...
                    normalized_name = attraction.lower().replace(' ', '') #normalize the name by forcing to lowercase and removing spaces
                    matching_attractions = [a for a in self.attractions if a.name.lower().replace(' ', '') == normalized_name] #Create a new list matching_attractions that contains all attractions from self.attractions whose names (after being converted to lowercase and having spaces removed) match the normalized_name of the current attraction in the attractions list.

                    if not matching_attractions: #if it is not a matching attraction...
                        with open('log.txt', 'a') as log: #open our text file with the intention to append
                            log.write(f"Error: No such attraction '{attraction}' in the theme park.\n") #We then say which attraction is not in the park
                    else:
                        for matching_attraction in matching_attractions: #Otheriwse...
                            matching_attraction.min_height = max(matching_attraction.min_height, height) #This line updates the min_height attribute of the current matching_attraction to be the maximum of its current min_height and the height variable. This effectively sets the min_height of the attraction to be the higher of the two values. 

        print("\nOverview of the attractions after security update:\n") #We then in a new line print an overview of this update.
        for attraction in self.attractions:
            print(f"- {attraction.name}: {attraction.min_height} cm") #For every attraction in the attractions list we print it's name and min height requirement.


# create theme park
efteling = ThemePark("The Efteling")

efteling.printOverview()

efteling.addAttraction(pagode)
efteling.printOverview()

efteling.addAttraction(max_moritz)
efteling.addAttraction(baron)
efteling.printOverview()

efteling.securityUpdate('update.txt')