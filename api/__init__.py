import os
import json
import csv

import requests

from ..config import access_token, var_to_ord
from . import items
from . import variations
from . import modifiers
from . import categories
from . import fees
from . import pages


rooturl = 'https://connect.squareup.com/v1'
headers = {'Authorization': 'Bearer ' + access_token,
           'Accept':        'application/json',
           'Content-Type':  'application/json'}


def get_locations():
    if os.path.isfile('locations.json'):
        with open('locations.json') as f:
            return json.load(f)
    else:
        r = requests.get(rooturl+'/me/locations', headers=headers)
        locs = r.json()
        loc_dict = {x['name']: x for x in locs}
        with open('locations.json', 'w') as f:
            json.dump(loc_dict, f)
        return loc_dict


locations = get_locations()


def size_ordinal(variation):
    '''
    Gets a variations ordinal from a diction. If it isn't in the dictionary,
    a '1' is returned.
    '''
    if variation in var_to_ord:
        return var_to_ord[variation]
    else:
        return '1'


def makeitems(csvfile):
    '''
    Takes a csv with Name, Variation, Price, and Category columns and
    a dictionary for ordinal lookup. Creates a dictionary with the item
    name as the key and creates a json structure for the item and its
    variations. Categories will have to be created before items can be
    assigned as the categories_id is needed.

    item = {
        'name': string,
        'variations': [{
            'name': string defaults to Regual if none,
            'ordinal': '1' default,
            'currency_code': 'USD',
            'pricing_type': 'VARIABLE_PRICING' or 'FIXED_PRICING'
            'price_money': {
                'currency_code': 'USD',
                'amount': cents
            }
        },
        {variation 2 ...}
        ]
        'category': category name
    }
    '''
    with open(csvfile) as f:
        fromcsv = list(csv.DictReader(f))

    file_items = {}
    for item in fromcsv:
        if item['Name'] not in file_items:
            file_items[item['Name']] = {
                    'name': item['Name'],
                    'variations': [],
                    'category': {'name': item['Category']}
            }
        variation = {
            'name': item['Variation'] if item['Variation'] else 'Regular',
            'ordinal': size_ordinal(item['Variation'])
        }
        if item['Price']:
            variation['price_money'] = {
                'currency_code': 'USD',
                'amount': int(float(item['Price'])*100)
            }
        else:
            variation['pricing_type'] = 'VARIABLE_PRICING'
        file_items[item['Name']]['variations'].append(variation)
    return file_items


def map_to_loc(f, locs):
    '''Applies function f to the store or list of stores.
    Returns iterable.
    '''
    if locs == 'all':
        locs = locations.keys()
    locs = list(locs)
    return map(f, locs)


def create_category(name, store_id):
    url = rooturl + store_id + '/categories'
    r = requests.post(url, headers=headers, json={'name': name})
    r.raise_for_status()
    return r.json()


def batch(reqs):
    '''
    Takes a list of requests in json
    '''
    if type(reqs) is not list:
        reqs = [reqs]
    batch_url = rooturl + '/batch'
    resp = []
    for sublist in [reqs[i:i+30] for i in range(0, len(reqs), 30)]:
        batch_req = {'requests': []}
        for req in sublist:
            batch_req['requests'].append(req)
        try:
            r = requests.post(batch_url, json=batch_req)
        except requests.exceptions.RequestException as e:
            print(e)
        else:
            resp += r.json()
    return resp


def update_items(csvfile):
    '''Updates item information

    Retrieves all items and categories from all locations,
    compares with the csvfile, creates items/variations/categories if need.
    '''
    # Setup: load file
    new_items = makeitems(csvfile, var_to_ord)
    # Get current items for each store

    '''
    Iterate through file items
        Check if item/vaiation is in stores, add if needed.
        Update item/variation price.
        Check/Update item category and create if needed.
    '''
