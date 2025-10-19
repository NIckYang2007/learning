from pathlib import Path

path1=Path('cats.txt')
path2=Path('dogs.txt')
try:
    cat_name=path1.read_text()
    dog_name=path2.read_text()
    print(f'{cat_name}\n{dog_name}')
except FileNotFoundError:
    #print('not find file')
    pass

"""记录特定文段在文章中出线次数"""
path3=Path('book.txt')
text=path3.read_text(encoding='utf-8')
a=True
b=""
while a:
    if b == '#':
        a = False
    else:
        b = input("word('#'):")
        output = text.lower().count(b)
        print(f'{b} 在文本中共出现了{output}次')

"""ValueError友好错误消息"""
while True:
    try:
        num1 = int(input("num1:"))
        num2 = int(input("num2:"))
        adding = num1 + num2
        print(adding)
    except ValueError:
        print('请勿输入字符')
















