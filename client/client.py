# cliente.py

import requests

BASE_URL = 'http://localhost:5000'

def get_articles():
    response = requests.get(f'{BASE_URL}/articles')
    return response.json()

def create_article(author, article_data):
    response = requests.post(f'{BASE_URL}/authors/{author}/articles', json=article_data)
    return response.json()

def update_article(author, article_id, article_data):
    response = requests.put(f'{BASE_URL}/authors/{author}/articles/{article_id}', json=article_data)
    return response.json()

def delete_article(author, article_id):
    response = requests.delete(f'{BASE_URL}/authors/{author}/articles/{article_id}')
    return response.json()

def get_comments(author):
    response = requests.get(f'{BASE_URL}/authors/{author}/comments')
    return response.json()

def create_comment(author, comment_data):
    response = requests.post(f'{BASE_URL}/authors/{author}/comments', json=comment_data)
    return response.json()

def update_comment(author, comment_id, comment_data):
    response = requests.put(f'{BASE_URL}/authors/{author}/comments/{comment_id}', json=comment_data)
    return response.json()

def delete_comment(author, comment_id):
    response = requests.delete(f'{BASE_URL}/authors/{author}/comments/{comment_id}')
    return response.json()
