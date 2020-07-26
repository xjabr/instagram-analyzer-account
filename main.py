import requests
from bs4 import BeautifulSoup
import json

username = str(input('Enter an username: '))

url_to_fetch = 'https://instagram.com/'+username+'/?__a=1'

res = requests.get(url_to_fetch)

if res.status_code == 404:
    print('Error: The account you searched not found!')
    exit(-1)

json_data = res.json()

user_data = json_data['graphql']['user']

print('User ID: {}'.format(user_data['id']))
print('Follower: {}'.format(user_data['edge_followed_by']['count']))
print('Follow: {}'.format(user_data['edge_follow']['count']))
print('Is Private: {}'.format(user_data['is_private']))
print('Is Verified: {}'.format(user_data['is_verified']))
print('Profile PIC: {}'.format(user_data['profile_pic_url_hd']))