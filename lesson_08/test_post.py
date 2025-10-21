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
 
def test_create_project_positive():
    resp = requests.post (base_url+ '/auth/companies', json=creds )
    id=resp.json()['content'][0]['id']
    
    auth = {
    'login': login,
    'password' : password,
    'companyId' : id
            }               

    resp = requests.post (base_url+ '/auth/keys/get', json=auth )
    key = resp.json()[0]['key']
    
    data = {
        'title' : 'Project_Zebra'
            }
    my_headers = {
        'Authorization' : f'Bearer {key}'
                 }
    resp = requests.post(base_url+ '/projects', json=data, headers=my_headers)
    project_id=resp.json()
    assert resp.status_code == 201


  #создание проекта с пустым заголовком  
def test_create_project_negative():
    resp = requests.post (base_url+ '/auth/companies', json=creds )
    id=resp.json()['content'][0]['id']
    
    auth = {
    'login': login,
    'password' : password,
    'companyId' : id
            }               

    resp = requests.post (base_url+ '/auth/keys/get', json=auth )
    key = resp.json()[0]['key']
    
    data = {
        'title' : ''
            }
    my_headers = {
        'Authorization' : f'Bearer {key}'
                 }
    resp = requests.post(base_url+ '/projects', json=data, headers=my_headers)
    assert resp.status_code == 201

    

 
