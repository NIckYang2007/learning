"""分别定义特权者和管理员的类"""

from lei import User

class Privileges:
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]

    def show_privileges(self):
        for a in self.privileges:
            print(a.title())
'''输出特权者的特权'''

class Admin(User):
    def __init__(self,first_name,last_name,gender="unknown",login_attempts=0):
        super().__init__(first_name,last_name,gender,login_attempts)

        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.login_attempts=login_attempts

        #self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()

    def print_name(self):
        print(f'your name is {self.first_name} {self.last_name}')
'''输出管理员的姓与名'''