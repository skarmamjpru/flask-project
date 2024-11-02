from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Blog  

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app) 

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
    app.run(debug=True, port=8000)
