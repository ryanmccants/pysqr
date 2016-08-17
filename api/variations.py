from ..config import access_token


'''
variation = {
  "pricing_type": "FIXED_PRICING",
  "track_inventory": true,
  "inventory_alert_type": "LOW_QUANTITY",
  "id": "cb890728-cfdc-4690-9e03-349f964f756r",
  "name": "Small",
  "price_money": {
    "currency_code": "USD",
    "amount": 400
  },
  "ordinal": 0,
  "item_id": "442d1344-6d2b-4238-83d0-0284dfd335d8",
  "inventory_alert_threshold": 10,
  "user_data": "SEASONAL=TRUE"
}
'''


def create_variation(variation, item, loc_id):
    ''' Creates variation '''
    req_id = '{} item {} variation create'.format(loc_id, item['id'])
    allowed = [
        'id',
        'name',
        'pricing_type',
        'price_money',
        'sku',
        'track_inventory',
        'inventory_alert_type',
        'inventory_alert_threshold',
        'user_data'
    ]
    body = {k: v for k, v in variation.items() if k in allowed}
    req = {
        'method': 'POST',
        'relative_path': ('/v1/{}/items/{}/variations'
                          .format(loc_id,)),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def update_variation(variation, item, loc_id):
    ''' Updates variation '''
    req_id = ('{} item {} variation {} update'
              .format(loc_id, item['id'], variation['id']))
    allowed = [
        'name',
        'pricing_type',
        'price_money',
        'sku',
        'track_inventory',
        'inventory_alert_type',
        'inventory_alert_threshold',
        'user_data'
    ]
    body = {k: v for k, v in variation.items() if k in allowed}
    req = {
        'method': 'PUT',
        'relative_path': ('/v1/{}/items/{}/variations/{}'
                          .format(loc_id, item['id'], variation['id'])),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def delete_variation(variation, item, loc_id):
    ''' Deletes variation '''
    req_id = '{} item {} variation {} delete'.format(loc_id, variation['id'])
    req = {
        'method': 'DELETE',
        'relative_path': ('/v1/{}/items/{}/variations/{}'
                          .format(loc_id, item['id'], variation['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req
