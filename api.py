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


def makeitems(csvfile, o_dict):
    '''
    Takes a csv with Name, Variation, Price, and Category columns and
    a dictionary for ordinal lookup. Creates a dictionary with the item
    name as the key and creates a json structure for the item and its
    variations. Categories will have to be created before items can be
    assigned as the categories_id is needed.
    '''
    with open(csvfile) as f:
        fromcvs = list(csv.DictReader(f))

    items = {}
    for item in fromcsv:
        if item['Name'] not in items:
            items[item['Name']] = {
                    'name': item['Name'],
                    'variations': [],
                    'category':{'name',item['Category']}
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
    r = requests.post(url, headers=headers, json={'name': name})
    r.raise_for_status()
    return r.json()


def create_item(item, store_id):
    url = rooturl + '/v1/' + store_id + 'item'
    r = requests.post(url, headers=headers, json=item)



