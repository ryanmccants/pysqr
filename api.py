import json
import csv

import requests

from config import api_token, var_to_ord


rooturl = 'https://connect.squareup.com/v1'
headers = {'Authorization': 'Bearer ' + api_token,
           'Accept':        'application/json',
           'Content-Type':  'application/json'}

def size_ordinal(variation, o_dict):
    '''
    Gets a variations ordinal from a diction. If it isn't in the dictionary,
    a '1' is returned.
    '''
    if variation in o_dict:
        return o_dict[variation]
    else:
        return '1'

def makeitems(fromcsv, o_dict):
    '''
    Takes a csv with Name, Variation, Price, and Category columns and
    a dictionary for ordinal lookup. Creates a dictionary with the item
    name as the key and creates a json structure for the item and its 
    variations. Categories will have to be created before items can be
    assigned as the categories_id is needed.
    '''
    items = {}
    for item in fromcsv:
        if item['Name'] not in items:
            items[item['Name']] = {'name': item['Name'],
                                   'variations': []
            }
        variation = {
            'name': item['Variation'] if item['Variation'] else 'Regular',
            'ordinal': size_ordinal(item['Variation']) if item['Variation'] else '1'
        }
        if item['Price']:
            variation['price_money'] = {
                'currency_code': 'USD',
                'amount': int(float(item['Price'])*100)
            }
        else:
            variation['pricing_type'] = 'VARIABLE_PRICING'
        items[item['Name']]['variations'].append(variation)
    return items

def create_category(name, store_id):
    url = rooturl + store_id + '/categories'
    r = post(url, headers=headers, json={'name': name})
    r.raise_for_status()
    return r.json()

def create_item(item, store_id):
    url = rooturl + '/v1/' + store_id + 'item'
    r = post(url, headers=headers, json=item)

def batch(reqs):
    batch_url = rooturl + '/batch'
    for sublist in [reqs[i:i+30] for i in range(0, len(reqs), 30)]:
        batch_req = {'requests': []}
        for req in sublist:
            batch_req['requests'].append(req)
        try:    
            resp = requests.post(batch_url, json=batch_req)
        except requests.exceptions.RequestException as e:
            print(e)

