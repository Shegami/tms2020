with open('dataset_3378_2.txt', 'r') as link:
    str = link.readline().strip()
import requests
print(str)
r = requests.get(str)
str2 = r.text.splitlines()
print(len(str2))