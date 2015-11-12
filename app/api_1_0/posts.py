from . import api
from flask import request, jsonify
from ..models import Post, Permission
from .. import db
from .authentication import auth
from .decorators import permission_required
from .errors import forbidden


@api.route('/posts/', methods=['POST'])
@permission_required(Permission.WRITE_ARTICLES)
def new_post():
    post = Post.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201, \
           {'Location': url_for('api.get_post', id=post.id, _external=True)}

@api.route('/posts/')
@auth.login_required
def get_posts():
    posts = Post.query.all()
    return jsonify({ 'posts': [post.to_json() for post in posts] })

@api.route('/posts/<int:id>')
@auth.login_required
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())

@api.route('/posts/<int:id>', methods=['PUT'])
@permission_required(Permission.WRITE_ARTICLES)
def edit_post(id):
    post = Post.query.get_or_404(id)
    if g.current_user != post.authur and \
            not g.current_user.can(Permission.WRITE_ARTICLES):
        return forbidden('Insufficient permissions')
        post.body = request.json.get('body', post.body)
    db.session.add(post)
    return jsonify(post.to_json())