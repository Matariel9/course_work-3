from flask import Flask, request, render_template,jsonify
from utilis import *

app = Flask(__name__)

__data = get_posts_all()

@app.route('/')
def main_page():
  return render_template('index.html', data = __data, lent = length(__data))

@app.route('/user-feed/<name>')
def user_feed(name):
  data = get_posts_by_user(name, __data)
  return render_template('user-feed.html', data = data, lent = length(data))

@app.route('/post/<int:pk>')
def post(pk):
  data = get_posts_by_pk(pk ,__data)
  comments = get_comments_by_post_id(pk, __data)
  return render_template('post.html', data = data, commRange = len(comments), comments = comments)

@app.route('/search/')
def search():
  search_by = request.args['s']
  found = search_for_posts(search_by, __data)
  return render_template('search.html', found = found, lent = length(found))


@app.route('/api/posts', methods=['GET'])
def api_posts():
  return jsonify(__data)

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def api_post_one(post_id):
  data = get_posts_by_pk(post_id, __data)
  return jsonify(data)

app.config['JSON_AS_ASCII'] = False
app.run()