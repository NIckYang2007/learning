def show_message(list):
    for a in list:
        print(a)

def send_message(text,new_list):
    text.reverse()
    while text:
        a=text.pop()
        print(a)
        new_list.append(a)

def shoow_message(text,new_list):
    print(text)
    print(new_list)

text=['hello','bye']
new_list=[]
show_message(text)
send_message(text,new_list)
shoow_message(text,new_list)
print(text)

def sandwich(*items):
    for a in items:
        print(f'you add {a} in your food')
sandwich('apple','peal')
sandwich('caa','ssa')

def build_profile(first, last, **user_info):
 
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('nick','yang',home='beijing'\
,gender='male')
print(user_profile)

def cars(manufactory,model,**items):
    items['manufactory']=manufactory
    items['model']=model
    return items
car = cars('subaru', 'outback', color='blue',
tow_package=True)
print(car)