import requests
import json
import random
import string

email = input('Enter email  ')
name = input('Enter name  ')


def generate_random_password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    password = []
    for i in range(10):
        password.append(random.choice(characters))
    random.shuffle(password)
    return ("".join(password))


password = generate_random_password()


def registration(email, password, username):
    session = requests.Session()
    register_url = 'https://discord.com/api/v9/auth/register'
    headers = {
        'referer': 'https://discord.com/register'
    }
    data = {
        'consent': True,
        'date_of_birth': '19900101',
        'email': email,
        'gift_code_sku_id': None,
        'invite': None,
        'password': password,
        'username': username,
        'captcha_key': None
    }
    session.post(register_url, headers=headers, json=data).json()


def get_token(email, password):
    login_url = 'https://discord.com/api/v9/auth/login'
    data = {
        'email': email,
        'password': password,
        'captcha_key': None,
        'gift_code_sku_id': None,
        'login_source': None,
        'undelete': False
    }
    token_response = requests.post(login_url, json=data)
    print(json.loads(token_response.text)['token'])


registration(email, password, name)
get_token(email, password)
