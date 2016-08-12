from config import access_token
'''
{
  "id": "442d1344-6d2b-4238-83d0-0284dfd335d8",
  "name": "Milkshake",
  "description": "It's better than yours",
  "category_id": 203498,
  'color': '',
  'abbreviation': '',
  "type": "NORMAL",
  "visibility": "PRIVATE",
  "available_online": false,
  "variations": [
    {
      "id": "cb890728-cfdc-4690-9e03-349f964f756r",
      "name": "Small",
      "pricing_type": "FIXED_PRICING",
      "price_money": {
        "currency_code": "USD",
        "amount": 400
      },
      "ordinal": 0,
      "item_id": "442d1344-6d2b-4238-83d0-0284dfd335d8"
    }
  ]
}
'''


def create_item(item, loc_id):
    ''' Creates item '''
    req_id = '{} item create'.format(loc_id)
    allowed = [
        'id',
        'name',
        'description',
        'category_id',
        'color',
        'abbreviation',
        'visibility',
        'available_online',
        'available_for_pickup',
        'variations'
    ]
    body = {k: v for k, v in item.items() if k in allowed}

    req = {
        'method': 'POST',
        'relative_path': '/v1/{}/items'.format(loc_id),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
    }
    return req


def list_items(loc_id):
    ''' Retrieves items for a given location. Defaults to all.'''
    req_id = '{} item list'.format(loc_id)
    req = {
        'method': 'GET',
        'relative_path': '/v1/{}/items'.format(loc_id),
        'access_token': access_token,
        'request_id': req_id
    }
    return req


def retrieve_item(item, loc_id):
    ''' Retrieves item '''
    req_id = '{} item {} retrieve'.format(loc_id, item['id'])
    req = {
        'method': 'GET',
        'relative_path': '/v1/{}/items/{}'.format(loc_id, item['id']),
        'access_token': access_token,
        'request_id': req_id
    }
    return req


def update_item(item, loc_id):
    ''' Updates item '''
    req_id = '{} item {} update'.format(loc_id, item['id'])
    allowed = [
        'name',
        'description',
        'category_id',
        'color',
        'abbreviation',
        'visibility',
        'available_online',
        'available_for_pickup'
    ]
    body = {k: v for k, v in item.items() if k in allowed}
    req = {
        'method': 'PUT',
        'relative_path': '/v1/{}/items/{}'.format(loc_id, item['id']),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
    }
    return req


def delete_item(item, loc_id):
    ''' Deletes item '''
    req_id = '{} item delete {}'.format(loc_id, item['name'])
    req = {
        'method': 'DELETE',
        'relative_path': '/v1/{}/items/{}'.format(loc_id, item['id']),
        'access_token': access_token,
        'request_id': req_id
    }
    return req
