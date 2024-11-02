from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Define the Blog model


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255))

# (Optional) Define additional User model for account functionality if needed


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    bio = db.Column(db.String(255))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    blogs = Blog.query.all()
    return render_template('home.html', title='Home', blogs=blogs)


@app.route('/account')
def account():
    return render_template('account.html', title='Account', user={'name': 'Skarma', 'bio': 'M.Tech'})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = Blog.query.get(blog_id)
    return render_template('blog_detail.html', blog=blog) if blog else "Blog not found", 404


@app.route('/search')
def search():
    query = request.args.get('query')
    search_results = Blog.query.filter(
        Blog.title.ilike(f'%{query}%')).all() if query else []
    return render_template('home.html', title='Search Results', blogs=search_results)


if __name__ == '__main__':
    app.run(debug=True)
