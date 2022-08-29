from gamersgrotto import db
from gamersgrotto.models.listings import Listing
from gamersgrotto.models.users import User
from gamersgrotto.models.posts import Post
from gamersgrotto.models.comments import Comment

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()
