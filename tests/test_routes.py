import json
from conftest import api

def test_base_routes(api):
    resp = api.get('/')
    assert resp.status == '200 OK'

def test_comments_routes(api):
    resp = api.get('/comments/')
    assert resp.status == '200 OK'

def test_posts_routes(api):
    resp = api.get('/posts')
    assert resp.status == '200 OK'

def test_listings_routes(api):
    resp = api.get('/listings/')
    assert resp.status == '200 OK'

def test_scores_routes(api):
    resp = api.get('/scores/')
    assert resp.status == '200 OK'

def test_listing_post_routes(api):
    mock_data = {
        'type':'sell',
        'price':'4',
        'title':'testtitle1',
        'description':'testdescription1',
        'image':'testimage1',
        'username':'testusername1',
        'location':'testlocation1',
        'marketstatus':'testmarketstatus1',
        'date':'01/09/2022'
    }
    resp = api.post('/listings', data=mock_data)
    assert resp.status == '308 PERMANENT REDIRECT'



def test_post_post_routes(api):
    mock_data = {
        'id':1,
        'title':'test1',
        'text': 'testtext1',
        'username':'testuser1',
        'likes':1,
        'dislikes':0
    }
    resp = api.post('/posts/', data=mock_data)
    assert resp.status == '404 NOT FOUND'

def test__score_post_routes(api):
    mock_data = {
        'id':1,
        'username':'test1',
        'score':6
    }
    resp = api.post('/scores', data=mock_data)
    assert resp.status == '308 PERMANENT REDIRECT'
