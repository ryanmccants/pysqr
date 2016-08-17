from ..config import access_token


'''
fee = {
  "calculation_phase": "FEE_SUBTOTAL_PHASE",
  "adjustment_type": "TAX",
  "applies_to_custom_amounts": true,
  "enabled": true,
  "inclusion_type": "ADDITIVE",
  "id": "19498df7-3fb0-4c96-8b47-860480718abk",
  "name": "Sales tax",
  "rate": "0.06",
  "type": "US_SALES_TAX"
}
'''


def create_fee(fee, loc_id):
    ''' Creates fee '''
    req_id = '{} fee create'.format(loc_id,)
    allowed = [
        'id',
        'name',
        'rate',
        'calculation_phase',
        'adjustment_type',
        'applies_to_custom_amounts',
        'enabled',
        'inclusion_type'
    ]
    body = {k: v for k, v in fee.items() if k in allowed}
    req = {
        'method': 'POST',
        'relative_path': '/v1/{}/fees'.format(loc_id),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def list_fees(loc_id):
    ''' Retrieves fees for a given location. Defaults to all.'''
    req_id = '{} fee list'.format(loc_id)
    req = {
        'method': 'GET',
        'relative_path': '/v1/{}/fees'.format(loc_id),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def retrieve_fee(fee, loc_id):
    ''' Retrieves fee '''
    req_id = '{} fee {} retrieve'.format(loc_id, fee['id'])
    req = {
        'method': 'GET',
        'relative_path': ('/v1/{}/fees/{}'
                          .format(loc_id, fee['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def update_fee(fee, loc_id):
    ''' Updates fee '''
    req_id = '{} fee {} update'.format(loc_id, fee['id'])
    allowed = [
        'name',
        'rate',
        'calculation_phase',
        'adjustment_type',
        'applies_to_custom_amounts',
        'enabled',
        'inclusion_type'
    ]
    body = {k: v for k, v in fee.items() if k in allowed}
    req = {
        'method': 'PUT',
        'relative_path': ('/v1/{}/fees/{}'
                          .format(loc_id, fee['id'])),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def delete_fee(fee, loc_id):
    ''' Deletes fee '''
    req_id = '{} fee {} delete'.format(loc_id, fee['id'])
    req = {
        'method': 'DELETE',
        'relative_path': ('/v1/{}/modifier-lists/{}'
                          .format(loc_id, fee['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def apply_fee(fee, item, loc_id):
    ''' Applies fee to item'''
    req_id = ('{} item {} fee {} apply'
              .format(loc_id, item['id'], fee['id']))
    req = {
        'method': 'PUT',
        'relative_path': ('/v1/{}/items/{}/modifier-lists/{}'
                          .format(loc_id, item['id'], fee['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def remove_fee(fee, item, loc_id):
    ''' Removes fee from item'''
    req_id = ('{} item {} fee {} remove'
              .format(loc_id, item['id'], fee['id']))
    req = {
        'method': 'DELETE',
        'relative_path': ('/v1/{}/items/{}/modifier-lists/{}'
                          .format(loc_id, item['id'], fee['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req
