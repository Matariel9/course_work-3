import app,pytest
from requests import get

def test_post_api():
    response = get('http://127.0.0.1:5000/post/1')
    print(response)

def test_posts_api():
    response = get('http://127.0.0.1:5000/')
    print(response)
#def test_posts_api(self, test_client):
    #response=main.test_client().get('/api/posts')
    #return response

#def test_post_api(self, test_client, num):
    #response=main.test_client().get(f'/api/{num}')
    #return response