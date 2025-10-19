"""测试调用txt文件"""
from importlib.resources import contents
from pathlib import Path

file=Path('learning.txt')
text=file.read_text()

for a in text.splitlines():
    b=a.replace('python','C')
    print(b)

print(text)

file.write_text(str(9))

"""存储用户姓名"""

try:
    print(9/0)
except ZeroDivisionError:
    print('you cant do it')

from pathlib import Path
file=Path("C:/Users/13520/Desktop/pro.txt")
name_list=[]

sign=True
while sign:
    name=input('please sign your name in here:')

    if name=='quit':
        sign=False
    else:
        name_list.append(name)

end=""
for a in name_list:
    end+=f'{a}\n'
file.write_text(end)

from pathlib import Path

def num_book(name):
    path=Path(name)
    try:
        book=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'the {name} is not exist')
    else:
        words=book.split()
        num=len(words)
        print(num)

name=input('text the name of book:')
num_book(f"{name}.txt")


