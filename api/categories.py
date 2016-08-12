from config import access_token


'''
category = {
  "id": "36ac7016-3a4e-4934-81f1-9057ac613f2y",
  "name": "Beverages"
}
'''


def create_category(category, loc_id):
    ''' Creates category '''
    req_id = '{} category create'.format(loc_id,)
    allowed = [
        'id',
        'name'
    ]
    body = {k: v for k, v in category.items() if k in allowed}
    req = {
        'method': 'POST',
        'relative_path': '/v1/{}/categories'.format(loc_id),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
        }
    return req


def list_categorys(loc_id):
    ''' Retrieves categorys for a given location. Defaults to all.'''
    req_id = '{} category list'.format(loc_id)
    req = {
        'method': 'GET',
        'relative_path': '/v1/{}/categories'.format(loc_id),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def retrieve_category(category, loc_id):
    ''' Retrieves category '''
    req_id = '{} category {} retrieve'.format(loc_id, category['id'])
    req = {
        'method': 'GET',
        'relative_path': ('/v1/{}/categories/{}'
                          .format(loc_id, category['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req


def update_category(category, loc_id):
    ''' Updates category '''
    req_id = '{} category {} update'.format(loc_id, category['id'])
    req = {
        'method': 'PUT',
        'relative_path': ('/v1/{}/categories/{}'
                          .format(loc_id, category['id'])),
        'access_token': access_token,
        'body': {'name': category['name']},
        'request_id': req_id
        }
    return req


def delete_category(category, loc_id):
    ''' Deletes category '''
    req_id = '{} category {} delete'.format(loc_id, category['id'])
    req = {
        'method': 'DELETE',
        'relative_path': ('/v1/{}/categories/{}'
                          .format(loc_id, category['id'])),
        'access_token': access_token,
        'request_id': req_id
        }
    return req
