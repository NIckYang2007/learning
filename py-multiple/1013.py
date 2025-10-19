
from pathlib import Path
import json

path=Path('num.json')

if path.exists():
    num=path.read_text()
    content=json.loads(num)
    for key,value in content.items():
        print(f'{key}:{value}')
else:
    data={}
    num=input("my favourite num is:")
    name=input('my name is:')
    age=input('my age is:')
    data['num']=num
    data['name']=name
    data['age']=age
    content=json.dumps(data)
    path.write_text(content)


from pathlib import Path
import json
path = Path('username.json')

def great_user():
    contents = path.read_text()
    name = json.loads(contents)
    return name

def sign_user():
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

name=""
if path.exists():#检查特定的文件是否存在
    name=great_user()
    ans=input(f'{name} is you?')
    if ans == 'yes':
        print(f"Welcome back, {name}!")
    else:
        sign_user()
else:
    sign_user()