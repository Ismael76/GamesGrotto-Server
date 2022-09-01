from gamersgrotto.models.users import User
from gamersgrotto.models.posts import Post
from gamersgrotto.models.comments import Comment
from gamersgrotto.models.listings import Listing

def test_new_user():
    user = User('testuser1', 'testuser1@gmail.com', '12345678')
    assert user.email == 'testuser1@gmail.com'
    assert user.username == 'testuser1'
    assert user.password == '12345678'

def test_new_post():
    post = Post('testtitle1', 'testcontent1', 'testuser1', 0 , 0)
    assert post.title == 'testtitle1'
    assert post.text == 'testcontent1'
    assert post.username == 'testuser1'
    assert post.likes == 0
    assert post.dislikes == 0

def test_new_listing():
    user = Listing('testtitle1', 'testdescription1', 'testimage1', 'testusername1', 0 , "12/09/2022")
    assert user.title == 'testtitle1'
    assert user.description == 'testdescription1'
    assert user.image == 'testimage1'
    assert user.username == 'testusername1'
    assert user.marketstatus == 0
    assert user.date == "12/09/2022"

def test_new_comments():
    comment = Comment('testtext1', 'testuser1', 1, 0, 1)
    assert comment.text == 'testtext1'
    assert comment.username == 'testuser1'
    assert comment.post_id == 1
    assert comment.likes == 0
    assert comment.dislikes == 1
