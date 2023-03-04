from flask import Flask, request, render_template, redirect
import utils

POSTS_PATH = 'data/posts.json'
COMMENTS_PATH = 'data/comments.json'
BOOKMARKS_PATH = 'data/bookmarks.json'

app = Flask(__name__)


@app.route('/')
def main_page():
    posts_data = utils.get_posts_all(POSTS_PATH)
    comments_data = utils.get_posts_all(COMMENTS_PATH)
    bookmarks = utils.get_posts_all(BOOKMARKS_PATH)

    posts_data = utils.string_crop(posts_data)
    posts_data = utils.comments_count(posts_data, comments_data)

    bookmarks_quantity = len(bookmarks)

    return render_template('index.html', posts=posts_data, bookmarks_cuantity=bookmarks_quantity)


@app.route('/post/<int:post_id>')
def post_page(post_id):
    posts_data = utils.get_posts_all(POSTS_PATH)
    comments_data = utils.get_posts_all(COMMENTS_PATH)

    output_post = utils.get_comments_by_post_id(posts_data, post_id)
    tags = utils.get_tags(output_post)

    output_comments = []
    for comment in comments_data:
        if post_id == comment['post_id']:
            output_comments.append(comment)

    comments_quantity = len(output_comments)
    return render_template("post.html", comments=output_comments, quantity=comments_quantity, tags=tags)


if __name__ == '__main__':
    app.run()
