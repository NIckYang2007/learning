"""记录书籍的字数"""

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
num_book(f"C:/Users/13520/Desktop/{name}.txt")
