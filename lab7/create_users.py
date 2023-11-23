from app import app, db
from app.models import User

def create_users():
    with app.app_context():

        user1 = User(username='user1', email='user1@example.com', password='password1')
        user2 = User(username='user2', email='user2@example.com', password='password2')
        user3 = User(username='user3', email='user3@example.com', password='password3')


        db.session.add_all([user1, user2, user3])


        db.session.commit()

if __name__ == "__main__":
    create_users()