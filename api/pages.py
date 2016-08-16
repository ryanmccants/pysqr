from urllib import parse

from config import access_token

'''
page = {
  "id": "c87595ae-14a6-42d7-acb6-008fc8e7ed3g",
  "name": "Lunch Items",
  "page_index": 0,
  "cells": []
}
'''

def create_page(page, loc_id):
    ''' Creates page '''
    req_id = '{} page create'.format(loc_id)
    allowed = [
        'id',
        'name',
        'page_index'
    ]
    body = {k: v for k, v in page.items() if k in allowed}

    req = {
        'method': 'POST',
        'relative_path': '/v1/{}/pages'.format(loc_id),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
    }
    return req


def list_pages(loc_id):
    ''' Retrieves pages for a given location. Defaults to all.'''
    req_id = '{} page list'.format(loc_id)
    req = {
        'method': 'GET',
        'relative_path': '/v1/{}/pages'.format(loc_id),
        'access_token': access_token,
        'request_id': req_id
    }
    return req


def update_page(page, loc_id):
    ''' Updates page '''
    req_id = '{} page {} update'.format(loc_id, page['id'])
    allowed = [
        'name',
        'page_index'
    ]
    body = {k: v for k, v in page.items() if k in allowed}
    req = {
        'method': 'PUT',
        'relative_path': '/v1/{}/pages/{}'.format(loc_id, page['id']),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
    }
    return req


def delete_page(page, loc_id):
    ''' Deletes page '''
    req_id = '{} page delete {}'.format(loc_id, page['name'])
    req = {
        'method': 'DELETE',
        'relative_path': '/v1/{}/pages/{}'.format(loc_id, page['id']),
        'access_token': access_token,
        'request_id': req_id
    }
    return req


def update_cell(page, loc_id):
    ''' Updates cell '''
    req_id = '{} page {} cell update'.format(loc_id, page['id'])
    allowed = [
        'row',
        'column',
        'object_type',
        'object_id',
        'placeholder_type'
    ]
    body = {k: v for k, v in page.items() if k in allowed}
    req = {
        'method': 'PUT',
        'relative_path': '/v1/{}/pages/{}/cells'.format(loc_id, page['id']),
        'access_token': access_token,
        'body': body,
        'request_id': req_id
    }
    return req

def delete_cell(page, loc_id):
    ''' Updates cell '''
    req_id = '{} page {} cell delete'.format(loc_id, page['id'])
    allowed = [
        'row',
        'column'
    ]
    params = parse.urlencode({k: v for k, v in page.items() if k in allowed})
    req = {
        'method': 'DELETE',
        'relative_path': '/v1/{}/pages/{}/cells?{}'.format(loc_id, page['id'], params),
        'access_token': access_token,
        'request_id': req_id
    }
    return req
