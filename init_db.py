from gamersgrotto import db
from gamersgrotto.models.listings import Listing
from gamersgrotto.models.users import User

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()
