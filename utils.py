import json


def get_posts_all(path):
    with open(path, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data


def get_posts_by_user(posts_data, user_name) -> list:
    user_posts = []
    for post in posts_data:
        if user_name == posts_data['poster_name']:
            user_posts.append(post)
    return user_posts


def get_comments_by_post_id(comments_data, post_id) -> list:
    comments = []
    for comment in comments_data:
        if post_id == comment['post_id']:
            comments.append(comment)
    return comments


def search_for_posts(posts_data, query):
    query_posts = []
    for post in posts_data:
        if query in post['content']:
            query_posts.append(post)
    return query_posts


def get_post_by_pk(posts_data, pk):
    post_by_pk = {}
    for post in posts_data:
        if pk == post['pk']:
            post_by_pk = post
    return post_by_pk


def string_crop(posts_data):
    for post in posts_data:
        post["content"] = post["content"][:50]
    return posts_data


def get_tags(post):
    tags = []
    text = post['content'].split(' ')
    for word in text:
        if '#' in word:
            tag = word.replace('#', '')
            tags.append(tag)
    return tags


def comments_count(posts_data, comments_data):
    comments_match = []
    for post in posts_data:
        for comment in comments_data:
            if comment['post_id'] == post['pk']:
                comments_match.append(post['pk'])
            post['comment'] = comments_match.count(post['pk'])
    return posts_data
