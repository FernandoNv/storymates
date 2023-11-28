import requests

def get_request(url):
    response = requests.get(url)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return None

def put_request(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, json=data, headers=headers)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return None

def post_request(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return None

def delete_request(url):
    response = requests.delete(url)
    
def test_article_endpoints():
    base_url = 'http://127.0.0.1:5000'

    response = get_request(f'{base_url}/articles')
    print(response)

    article_id = 1
    response = get_request(f'{base_url}/articles/{article_id}')
    print(response)

    author = 'fernando'
    response = get_request(f'{base_url}/authors/{author}/articles')
    print(response)

    new_article_data = {'title': 'New Article', 'content': 'New content'}
    response = post_request(f'{base_url}/authors/{author}/articles', data=new_article_data)
    print(response)

    article_id = 3  
    update_article_data = {'title': 'Updated Article', 'content': 'Updated content'}
    response = put_request(f'{base_url}/authors/{author}/articles/{article_id}', data=update_article_data)
    print(response)

    delete_request(f'{base_url}/authors/{author}/articles/{article_id}')

def test_comment_endpoints():
    base_url = 'http://127.0.0.1:5000'

    article_id = 1
    new_comment_data = {'text': 'New Comment'}
    response = post_request(f'{base_url}/articles/{article_id}/comments', data=new_comment_data)
    print(response)

    comment_id = 1  
    update_comment_data = {'text': 'Updated Comment'}
    response = put_request(f'{base_url}/articles/{article_id}/comments/{comment_id}', data=update_comment_data)
    print(response)

    response = delete_request(f'{base_url}/articles/{article_id}/comments/{comment_id}')
    print(response)

if __name__ == '__main__':
    test_article_endpoints()