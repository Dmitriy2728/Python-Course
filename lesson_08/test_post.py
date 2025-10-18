import requests
import pytest

base_url = "https://yougile.com/api-v2"

def test_company_list():
    creds = {
        'login': 'd.palkin2728@gmail.com',
        'password' : '+_9DsjK!wY*#4Hf!',
        'name' : 'Поток 100.2'
    }
    resp = requests.post(base_url+'/auth/companies', json=creds)
    assert resp.status_code == 200
    body = resp.json()
    company_id = body['content'][0]['id']
    creds2= {
        'login': 'd.palkin2728@gmail.com',
        'password' : '+_9DsjK!wY*#4Hf!',
        'companyId' : company_id
    }
    resp2 = requests.post(base_url+'/auth/keys/get', json=creds2)
    body2 = resp2.json()
    key = body2[0]['key']
    
token = 'hdtg9AFgoacDJ1ccKduQ86KQIf32GDINs+6FByfoNOO7-tv6Z6nsQ+dpbBLVdHBu'
def test_create_project():
    my_headers = {
        'Authorization' : f'Bearer {token}',
        'Content-Type': 'application/json'
    }
      
    new_project = {
        'title' : 'Дождались',
        }
    resp3=requests.post(base_url +'/projects', json=new_project, headers=my_headers)
    body3=resp3.json()
    assert resp3.status_code == 201
    assert isinstance(body3.get("id"), str)
    assert body3["id"]
    print(body3)











