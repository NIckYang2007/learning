class Restaurant:

    def __init__(self,name,type,number_served=0):
        self.name=name
        self.type=type
        self.number_served=number_served

    def describe(self):
        print(f'{self.name},{self.type}')

    def open_restaurant(self):
        print('restaurant is opening')

    def set_number_served(self):
        print(f'there are {self.number_served} waiting')

    def increment_number_served(self,add):
        self.number_served +=add

#____________________________________________________________

class User:
    def __init__(self,first_name,last_name,gender,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.login_attempts=login_attempts

    def describe_user(self):
        print(f'your name is {self.first_name.title()} \
{self.last_name.title()} and your gender is {self.gender}')

    def greet_user(self):
        print(f'hello {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

#______________________________________________________________




