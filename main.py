from urllib.request import urlopen
import json
import pandas as pd
import pickle
import time

df = pd.read_csv('top500_domains.csv')

def get_domain_data(domain):
    ENDPOINT = 'http://us.api.semrush.com/?action=report&type=domain_rank_history&domain=%s'
    response = urlopen(ENDPOINT % (domain))
    data = response.read().decode('utf-8')
    return json.loads(data)

all_website_data = []
for index, row in df.iterrows():
    domain = row['URL']
    domain_data = get_domain_data(domain)
    all_website_data.append(domain_data['rank_history']['data'])
    print('Collected')
    time.sleep(1)


with open('data/all_domain_data.h5', 'w') as f:
    pickle.dump(all_website_data, f)
