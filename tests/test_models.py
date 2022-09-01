from gamersgrotto.models.users import User

def test_new_user():
    user = User('testuser1', 'testuser1@gmail.com', '12345678')
    assert user.email == 'testuser1@gmail.com'
    assert user.username == 'testuser1'
    assert user.password == '12345678'
