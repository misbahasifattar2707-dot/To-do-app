# # =============================================================================
# # Part 2: Database Setup
# # =============================================================================
# # Now we add a database to store data permanently.
# # We will learn:
# #   1. What is SQLAlchemy (database toolkit)
# #   2. How to create database models (tables)
# #   3. How to query the database
# # =============================================================================

# from flask import Flask, render_template
# from models import db, User, Todo, init_db

# app = Flask(__name__)

# # Database configuration
# # 'sqlite:///todo.db' creates a file called 'todo.db' in instance/ folder
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize the database
# init_db(app)


# # =============================================================================
# # ROUTES
# # =============================================================================

# @app.route('/')
# def home():
#     """Home page"""
#     return render_template('index.html')


# @app.route('/test-db')
# def test_db():
#     """
#     Test route to verify database is working.
#     Creates a test user and todo if they don't exist.
#     """
#     # Check if test user exists
#     user = User.query.filter_by(username='testuser').first()

#     if not user:
#         # Create test user
#         user = User(
#             username='testuser',
#             email='test@example.com',
#             password_hash='temporary'
#         )
#         db.session.add(user)
#         db.session.commit()

#         # Create test todo
#         todo = Todo(
#             task_content='Learn SQLAlchemy',
#             user_id=user.id
#         )
#         db.session.add(todo)
#         db.session.commit()

#     # Get all users and todos for display
#     all_users = User.query.all()
#     all_todos = Todo.query.all()

#     return render_template('test_db.html', users=all_users, todos=all_todos)


# # =============================================================================
# # RUN THE SERVER
# # =============================================================================
# if __name__ == '__main__':
#     print("\n" + "="*50)
#     print("  Part 2: Database Setup")
#     print("  Open: http://127.0.0.1:5000")
#     print("  Test DB: http://127.0.0.1:5000/test-db")
#     print("="*50 + "\n")
#     app.run(debug=True)


# # ============================================
# # SELF-STUDY QUESTIONS
# # ============================================
# # 1. What is SQLAlchemy and why do we use it?
# # 2. What does db.Column(db.String(80)) mean?
# # 3. What is the difference between db.session.add() and db.session.commit()?
# # 4. What does filter_by() do? How is it different from get()?
# # 5. What happens if you delete todo.db file and restart the app?
# #
# # ============================================
# # ACTIVITIES - Try These!
# # ============================================
# # Activity 1: Add a new field
# #   - In models.py, add 'phone' field to User model
# #   - Delete todo.db file (so tables are recreated)
# #   - Restart the app and check if it works
# #
# # Activity 2: Query practice
# #   - In test_db route, try: User.query.all() (gets all users)
# #   - Try: User.query.first() (gets first user)
# #   - Try: User.query.count() (counts users)
# #
# # Activity 3: View database file
# #   - Install "DB Browser for SQLite" software
# #   - Open instance/todo.db file
# #   - See the tables and data inside
# #
# # Activity 4: Add more test data
# #   - Modify test_db() to create 3 users instead of 1
# #   - Create different todos for each user
# # ============================================


from flask import Flask, render_template
from models import db, User, Todo, init_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test-db')
def test_db():
    # =========================
    # Activity 4: Create 3 users
    # =========================
    if User.query.count() == 0:
        user1 = User(
            username='alice',
            email='alice@example.com',
            phone='1111111111',
            password_hash='pass1'
        )
        user2 = User(
            username='bob',
            email='bob@example.com',
            phone='2222222222',
            password_hash='pass2'
        )
        user3 = User(
            username='charlie',
            email='charlie@example.com',
            phone='3333333333',
            password_hash='pass3',
            is_admin=True
        )

        db.session.add_all([user1, user2, user3])
        db.session.commit()

        todos = [
            Todo(task_content='Learn Flask', user_id=user1.id),
            Todo(task_content='Learn SQLAlchemy', user_id=user1.id),
            Todo(task_content='Build Todo App', user_id=user2.id),
            Todo(task_content='Test Database', user_id=user3.id),
        ]

        db.session.add_all(todos)
        db.session.commit()

    # =========================
    # Activity 2: Query practice
    # =========================
    all_users = User.query.all()
    first_user = User.query.first()
    user_count = User.query.count()

    print("ALL USERS:", all_users)
    print("FIRST USER:", first_user)
    print("USER COUNT:", user_count)

    all_todos = Todo.query.all()

    return render_template(
        'test_db.html',
        users=all_users,
        todos=all_todos
    )


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("  Part 2: Database Setup (Modified)")
    print("  Open: http://127.0.0.1:5000")
    print("  Test DB: http://127.0.0.1:5000/test-db")
    print("=" * 50 + "\n")
    app.run(debug=True)
