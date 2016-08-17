from ..config import access_token


'''
modlist = {
    "name": "Toppings",
    "selection_type": "MULTIPLE",
    "id": "dcd7e350-c50f-421f-ada1-23a825b008b2",
    "modifier_options": [
        {
            "name": "Whipped Cream",
            "id": "39059fd0-ae9d-4eb3-b6e8-dd3198f019b8",
            "on_by_default": false,
            "price_money": {
              "currency_code": "USD",
                "amount": 50
            }
            "ordinal": 0,
            "modifier_list_id": "dcd7e350-c50f-421f-ada1-23a825b008b2"
        }
    ]
}
'''


def create_modlist(modlist, loc_id):
    ''' Creates modlist '''
    req_id = '{} modlist create'.format(loc_id,)
    allowed = [
        'id',
        'name',
        'modifier_options',
        'selection_type'
    ]
    body = {k: v for k, v in modlist.items() if k in allowed}
    req = {
        'method': 'POST',
        'relative_path': '/v1/{}/modifier-lists'.format(loc_id),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def list_modlists(loc_id):
    ''' Retrieves modlists for a given location. Defaults to all.'''
    req_id = '{} modlist list'.format(loc_id)
    req = {
        'method': 'GET',
        'relative_path': '/v1/{}/modifier-lists'.format(loc_id),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def retrieve_modlist(modlist, loc_id):
    ''' Retrieves modlist '''
    req_id = '{} modlist {} retrieve'.format(loc_id, modlist['id'])
    req = {
        'method': 'GET',
        'relative_path': ('/v1/{}/modifier-lists/{}'
                          .format(loc_id, modlist['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def update_modlist(modlist, loc_id):
    ''' Updates modlist '''
    req_id = '{} modlist {} update'.format(loc_id, modlist['id'])
    allowed = [
        'name',
        'selection_type'
    ]
    body = {k: v for k, v in modlist.items() if k in allowed}
    req = {
        'method': 'PUT',
        'relative_path': ('/v1/{}/modifier-lists/{}'
                          .format(loc_id, modlist['id'])),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def delete_modlist(modlist, loc_id):
    ''' Deletes modlist '''
    req_id = '{} modlist {} delete'.format(loc_id, modlist['id'])
    req = {
        'method': 'DELETE',
        'relative_path': ('/v1/{}/modifier-lists/{}'
                          .format(loc_id, modlist['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def apply_modlist(modlist, item, loc_id):
    ''' Applies modlist to item'''
    req_id = ('{} item {} modlist {} apply'
              .format(loc_id, item['id'], modlist['id']))
    req = {
        'method': 'PUT',
        'relative_path': ('/v1/{}/items/{}/modifier-lists/{}'
                          .format(loc_id, item['id'], modlist['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def remove_modlist(modlist, item, loc_id):
    ''' Removes modlist from item'''
    req_id = ('{} item {} modlist {} remove'
              .format(loc_id, item['id'], modlist['id']))
    req = {
        'method': 'DELETE',
        'relative_path': ('/v1/{}/items/{}/modifier-lists/{}'
                          .format(loc_id, item['id'], modlist['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def create_modifier(modifier, modlist, loc_id):
    ''' Creates modifier '''
    req_id = ('{} modlist {} modifier create'
              .format(loc_id, modlist['id']))
    allowed = [
        'id',
        'name',
        'price_money',
        'on_by_default'
    ]
    body = {k: v for k, v in modifier.items() if k in allowed}
    req = {
        'method': 'POST',
        'relative_path': ('/v1/{}/modifier-lists/{}/modifier_options'
                          .format(loc_id, modlist['id'])),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def update_modifier(modifier, modlist, loc_id):
    ''' Updates modlist '''
    req_id = ('{} modlist {} modifier {} update'
              .format(loc_id, modlist['id'], modifier['id']))
    allowed = [
        'name',
        'selection_type'
    ]
    body = {k: v for k, v in modifier.items() if k in allowed}
    req = {
        'method': 'PUT',
        'relative_path': ('/v1/{}/modifier-lists/{}/modifier_options/{}'
                          .format(loc_id, modlist['id'])),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def delete_modifier(modifier, modlist, loc_id):
    ''' Deletes modlist '''
    req_id = ('{} modlist {} modifier {} delete'
              .format(loc_id, modlist['id'], modifier['id']))
    req = {
        'method': 'DELETE',
        'relative_path': ('/v1/{}/modifier-lists/{}/modifier_options/{}'
                          .format(loc_id, modlist['id'], modifier['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req
