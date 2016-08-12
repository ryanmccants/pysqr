from config import api_token


def create_item(item, loc_id):
    ''' Creates item '''
    req_id = '{} item create {}'.format(loc_id, item['name'])
    req = {
            'method': 'POST',
            'relative_path': '/v1/{}/items'.format(loc_id),
            'access_token': access_token,
            'body': item,
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
            # 'body': {},
            'request_id': req_id
            }
    return req


def retrieve_item(item, loc_id):
    ''' Retrieves item '''
    req_id = '{} item update {}'.format(loc_id, item['name'])
    req = {
            'method': 'GET',
            'relative_path': '/v1/{}/items/{}'.format(loc_id, item['id']),
            'access_token': access_token,
            'body': item,
            'request_id': req_id
            }
    return req


def update_item(item, loc_id):
    ''' Updates item '''
    req_id = '{} item update {}'.format(loc_id, item['name'])
    req = {
            'method': 'PUT',
            'relative_path': '/v1/{}/items/{}'.format(loc_id, item['id']),
            'access_token': access_token,
            'body': item,
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
            'body': item,
            'request_id': req_id
            }
    return req


