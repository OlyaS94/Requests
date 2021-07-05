#!/usr/bin/env python
# coding: utf-8

# In[25]:


import requests

search_url = "https://superheroapi.com/api/2619421814940190/search/"
heroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]


for hero in heroes:
    my_request = requests.get(search_url + hero['name'])
    
    hero['intelligence'] = int(my_request.json()['results'][0]['powerstats']['intelligence'])
    
print(sorted(heroes, key = lambda hero: - hero['intelligence'])[0]['name'])


# In[ ]:




