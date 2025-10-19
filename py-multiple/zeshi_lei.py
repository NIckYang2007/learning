from pdb import post_mortem
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





cantine=Restaurant('coco','5')
print(f'the name is {cantine.name},type\
 is {cantine.type}')

cantine.describe()
cantine.open_restaurant()
cantine.set_number_served()

cantine2=Restaurant('jaja','4',5)

cantine2.describe()
cantine2.increment_number_served(30)
cantine2.set_number_served()







class User:
    def __init__(self,first_name,last_name,gender,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.login_attempts=login_attempts

    def describe_user(self):
        print(f'your name is {self.first_name}\''
f' {self.last_name} and your gender is {self.gender}')

    def greet_user(self):
        print(f'hello {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

person1=User('nick','yang','male',10)

person1.describe_user()
person1.greet_user()
person1.increment_login_attempts()

print(f'{person1.login_attempts}')
print(f'you are {person1.gender}')

person1.reset_login_attempts()

print(person1.login_attempts)

'''继承'''
class Icecreamstand(Restaurant):
    def __init__(self,name,type,number_served=0):
        super().__init__(name,type,number_served)
        self.flavour=['a','b','c']

    def flavou(self):
        for a in self.flavour:
            print(a)

icecream=Icecreamstand('ciak','m',5)
icecream.flavou()

class Privileges:
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]

    def show_privileges(self):
        for a in self.privileges:
            print(a.title())

class Admin(User):
    def __init__(self,first_name,last_name,gender="unknown",login_attempts=0):
        super().__init__(first_name,last_name,gender,login_attempts)
        self.privileges=["can add post","can delete post","can ban user"]
        self.privileges=Privileges()




admin=Admin('nick','yang','male',9)
admin.privileges.show_privileges()



class Car:
     def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
     def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
     def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on\
\it.")
     def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
     def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self,battery_size):
        print(f"This car has a {battery_size}-kWh\
battery.")

    def upgrade_battery(self,battery_size):
        battery_size=65
        return battery_size


class ElectricCar(Car):
     def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery('')



my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.battery.upgrade_battery(input('请输入电量')))
