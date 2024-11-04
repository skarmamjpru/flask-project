from flask import jsonify, render_template, request
from .models import Blog, BlogSchema, db

blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)


def init_routes(app):
    @app.route('/')
    def home():
        blogs = Blog.query.all()
        print("Blogs fetched:", blogs)
        return render_template('home.html', title='Home', blogs=blogs)

    @app.route('/api/blogs/', methods=['GET'])
    def api_blogs_list():
        all_blogs = Blog.query.all()
        result = blogs_schema.dump(all_blogs)
        return jsonify(result)

    @app.route('/api/blogs/<int:blog_id>', methods=['GET'])
    def api_blog_detail(blog_id):
        blog = Blog.query.get(blog_id)
        if blog:
            return jsonify(blog_schema.dump(blog))
        else:
            return jsonify({"error": "Blog not found"}), 404

    @app.route('/blog/<int:blog_id>', methods=['GET'])
    def blog_detail(blog_id):
        blog = Blog.query.get(blog_id)
        if blog:
            return render_template('blog_detail.html', blog=blog)
        else:
            return jsonify({"error": "Blog not found"}), 404

    @app.route('/api/blogs/', methods=['POST'])
    def api_create_blog():
        title = request.json.get('title')
        content = request.json.get('content')
        author = request.json.get('author')
        image_url = request.json.get('image_url', '')

        new_blog = Blog(title=title, content=content,
                        author=author, image_url=image_url)
        db.session.add(new_blog)
        db.session.commit()
        return jsonify(blog_schema.dump(new_blog)), 201

    @app.route('/api/blogs/<int:blog_id>', methods=['PUT'])
    def api_update_blog(blog_id):
        blog = Blog.query.get(blog_id)
        if blog:
            blog.title = request.json.get('title', blog.title)
            blog.content = request.json.get('content', blog.content)
            blog.author = request.json.get('author', blog.author)
            blog.image_url = request.json.get('image_url', blog.image_url)

            db.session.commit()
            return jsonify(blog_schema.dump(blog))
        else:
            return jsonify({"error": "Blog not found"}), 404

    @app.route('/api/blogs/<int:blog_id>', methods=['DELETE'])
    def api_delete_blog(blog_id):
        blog = Blog.query.get(blog_id)
        if blog:
            db.session.delete(blog)
            db.session.commit()
            return jsonify({"message": "Blog deleted successfully"}), 200
        else:
            return jsonify({"error": "Blog not found"}), 404

    @app.route('/search')
    def search():
        query = request.args.get('query')
        search_results = Blog.query.filter(
            Blog.title.ilike(f'%{query}%')).all() if query else []
        return render_template('home.html', title='Search Results', blogs=search_results)

    @app.route('/account')
    def account():
        return render_template('account.html', title='Account', user={'name': 'Skarma', 'bio': 'M.Tech'})

    @app.route('/contact')
    def contact():
        return render_template('contact.html', title='Contact')
