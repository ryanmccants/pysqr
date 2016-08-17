def batch(reqs):
    '''
    Takes a list of requests in json
    '''
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
   
