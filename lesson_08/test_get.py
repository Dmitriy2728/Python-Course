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

# Запрашиваем поиск проекта по существующему ID
def test_get_project_with_id_positive():
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
        
    resp = requests.get(base_url+ '/projects/' + project_id, headers =my_headers)
    title = resp.json()['title']

    assert resp.status_code == 200
    assert title == 'UpdatedProject28'
  
# Запрашиваем поиск проекта по несуществующему ID
def test_get_project_with_id_negative():
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
    project_id= '6ac9c031-2222-1111-3333-0087c16004e8'
        
    resp = requests.get(base_url+ '/projects/' + project_id, headers =my_headers)
    title = resp.json()['title']

    assert resp.status_code == 200
    assert title == 'UpdatedProject28'

    