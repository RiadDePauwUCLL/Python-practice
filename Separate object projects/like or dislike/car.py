from l_make import car_make
from l_model import car_model
from l_year import car_year
from l_color import car_color

class Car:
  
    def __init__(self):
        self.make = car_make()
        self.model = car_model()
        self.year = car_year()

    def questions(self):
        print('\n' + f'Type in what kind of car you either like or dislike!' + '\n')
        self.question_make = input("What kind of car are you looking for? ")
        self.question_model = input("What is the model? ")
        self.question_year = input("What year is the car from? ")
        self.question_color = input("What kind of color do you want the car to have? ")

    def like(self):
        self.question_year = int(self.question_year)    
        if self.question_model in self.model:
            print('\n\n' + f'This {self.question_make} {self.question_model} {self.question_year} {self.question_color} is quite epic' + '\n')
        else:
            print('\n\n' + f'{self.question_make} {self.question_model} {self.question_year} {self.question_color}' + '\n')
            print(f'You have terrible taste in cars holy shit lmao' + '\n')
        
        if self.question_color == 'Green':
            print(f'Who the fuck PICKS GREEN AS A COLOR FOR THEIR CAR??? EWWWW')

    def dislike(self):
        self.question_year = int(self.question_year)    
        if self.question_model in self.model:
            print('\n' + f'This {self.question_make} {self.question_model} {self.question_year} {self.question_color} is a dogshit car' + '\n')
            print(f'What the fuck what is wrong with you' + '\n')
        else:
            print(f'{self.question_make} {self.question_model} {self.question_year} {self.question_color}' + '\n')
            print(f'Yeah no clue what that is but it probably stinks' + '\n')