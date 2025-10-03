user_name=['admin','nick','yang','wang','zhao']

if user_name:
    for name in user_name:
        if name=='admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {name.capitalize()}, thank you for logging in again.')
else:
    print('We need to find some users!')

#____________________________________________________

current_users=['nick','yang','zhang','huang','jiang']
new_users=['nick','xu','jack',"YANG"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} has been used")
    else:
        print(f"{new_user} is available")

#______________________________________________________

list=[a for a in range(1,10)]
for a in list:
    #print(a)
    if a==1:
        print('1st')
    elif a==2:
        print('2nd')
    elif a==3:
        print('3rd')
    else:
        print(f'{a}th')
