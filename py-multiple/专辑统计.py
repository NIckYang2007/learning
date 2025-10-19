def make_shirt(size,char='I love Python'):
    print(f'the size is {size}\n\
the char is {char}')
make_shirt(size='M')
make_shirt("s",char='haha')

def describe_city(city,country='china'):
    print(f'{city.title()} is \
in {country.title()}')
describe_city('shanghai')
describe_city('beijing')
describe_city('chongqin')
describe_city(country='usa',city='new york')

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

'''8.6'''
def city(city,country):
    return f'"{city.title()},{country.title()}"'
print(city('shanghai','china'))
print(city('newyork','usa'))

'''8.7'''


def album(singer,name,num=None):
    album_list={
        'singer':singer,
        'name':name,
        }
    if num:
        album_list['num']=num
    else:    
        album_list
    
    return album_list

print('输入quit以终止')
list=[]
singer=""
while True:
        singer=input('singer:')
        if singer=='quit':
            print('_____________')
            break
        name=input('name:')
        num=input('num:')

        list.append(album(singer,name,num))
for a in list:
    if 'num' in a:
        for c,d in a.items():
            print(f"{c}:{d}")
    else:
        for c,d,in a.items():
            print(f"{c}:{d}")
    print('.............')
    





     
   
        
    
