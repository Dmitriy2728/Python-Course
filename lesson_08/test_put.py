import requests
import pytest

base_url = "https://yougile.com/api-v2"
id = '4149782a-817d-40f7-a006-5e230b127323'
token = 'hdtg9AFgoacDJ1ccKduQ86KQIf32GDINs+6FByfoNOO7-tv6Z6nsQ+dpbBLVdHBu'

def test_change_project():
    my_headers = {
        'Authorization' : f'Bearer {token}',
        'Content-Type': 'application/json'
    }
      
    project_id = {
        'id' : f'{id}',
        }
    resp=requests.put(base_url +'/projects', json=project_id, headers=my_headers)
    body=resp.json()
    assert resp.status_code == 200
  