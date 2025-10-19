class Die:
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):

        import random
        num=random.randint(1,self.sides)
        print(num)

dice=Die()
for a in range(1,11):
    dice.roll_die()
print('___________')
dice2=Die(10)
for a in range(1,11):
    dice2.roll_die()
print('___________')
dice3=Die(20)
for a in range(1,11):
    dice3.roll_die()
print('___________')

num=['1','3','2','4','5','6','3','2','4','2','h','t','s']
list=[]
from random import choice
for a in range(1,5):
    b=choice(num)
    num.remove(b)

    list.append(b)
print(f'if your number is {list},you win')

import random
from lei2 import Admin
admin1=Admin('nick','yang')
admin1.print_name()

admin1.privileges.show_privileges()

admin1.describe_user()


