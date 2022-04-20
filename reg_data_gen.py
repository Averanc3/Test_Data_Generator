import csv
import random
from password_generator import PasswordGenerator

import names
from random_username.generate import generate_username

file_path = '/Users/nikitafadeenko/PycharmProjects/Python_HW1/'
file_name = 'reg_data_gen.csv'
full_path = file_path + file_name

def rand_post_agent():
    agents = ['yandex', 'mail', 'google']
    return agents[random.randint(0,len(agents)-1)]
def domain_zone():
    zones = ['ru', 'com', 'org', 'es', 'uk', 'fr', 'it']
    return zones[random.randint(0,len(zones)-1)]



pwo = PasswordGenerator()
print(pwo.generate())

n = 10
users = []
usernames = generate_username(n)
for i in range(n):
    user = []
    print(usernames[i])
    mail = usernames[i]+str(random.randint(101,998))+'@'+rand_post_agent()+'.'+domain_zone()
    print(mail)
    user.append(usernames[i])
    user.append(mail)
    user.append(names.get_first_name())
    user.append(names.get_last_name())
    user.append(pwo.generate())
    users.append(user)

print(users)



with open(full_path, 'w') as cf:
    writer = csv.writer(cf)
    writer.writerow(['login', 'mail', 'name', 'last_name', 'password'])
    writer.writerows(users)



