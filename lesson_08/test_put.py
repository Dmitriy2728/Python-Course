import requests
import pytest
from dotenv import load_dotenv
import os


base_url = "https://yougile.com/api-v2"

load_dotenv()
login = os.getenv("login")
password = os.getenv("password")

creds = {
    'login': login,
    'password' : password,
    'name' : 'Поток 100.2'
        }

def test_change_project_positive():
    resp = requests.post (base_url+ '/auth/companies', json=creds )
    id=resp.json()['content'][0]['id']
    
    auth = {
    'login': login,
    'password' : password,
    'companyId' : id
            }               

    resp = requests.post (base_url+ '/auth/keys/get', json=auth )
    key = resp.json()[0]['key']
    
    my_headers = {
        'Authorization' : f'Bearer {key}'
                 }
    project_id= '6ac9c031-0307-4918-8e85-0087c16004e8'
    data = {
        'title' : 'UpdatedProject28'
            }    
    resp = requests.put(base_url+ '/projects/' + project_id, headers =my_headers, json=data)
    assert resp.status_code == 200
  
  #проверяем обновился ли заголовок проекта, запрашивая его по ID
    resp = requests.get(base_url+ '/projects/' + project_id, headers =my_headers)
    body = resp.json()['title']

    assert resp.status_code == 200
    assert body == 'UpdatedProject28'

#делаем изменение проекта, присваивая пустой заголовок
def test_change_project_negative():
    resp = requests.post (base_url+ '/auth/companies', json=creds )
    id=resp.json()['content'][0]['id']
    
    auth = {
    'login': login,
    'password' : password,
    'companyId' : id
            }               

    resp = requests.post (base_url+ '/auth/keys/get', json=auth )
    key = resp.json()[0]['key']
    
    my_headers = {
        'Authorization' : f'Bearer {key}'
                 }
    project_id= '6ac9c031-0307-4918-8e85-0087c16004e8'
    data = {
        'title' : ''
            }    
    resp = requests.put(base_url+ '/projects/' + project_id, headers =my_headers, json=data)
    assert resp.status_code == 200
  
 