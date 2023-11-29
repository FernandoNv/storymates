# Mock data for articles
mock_articles = [
    {'id': 1, 'title': 'Introduction to Python', 'content': 'Python is a versatile programming language.'},
    {'id': 2, 'title': 'Web Development with Flask', 'content': 'Building web applications using Flask framework.'},
    {'id': 3, 'title': 'Data Science with Pandas', 'content': 'Analyzing and manipulating data using Pandas library.'},
]

# Mock data for comments
mock_comments = [
    {'id': 1, 'content': 'Great article!', 'article_id': 1},
    {'id': 2, 'content': 'I learned a lot.', 'article_id': 1},
    {'id': 3, 'content': 'Looking forward to more tutorials.', 'article_id': 2},
    {'id': 4, 'content': 'Nice explanation of Pandas functions.', 'article_id': 3},
    {'id': 5, 'content': 'Could you provide more examples?', 'article_id': 3},
]

# Functions to retrieve mock data
def get_articles():
    return mock_articles

def get_article_by_id(article_id):
    return next((article for article in mock_articles if article['id'] == article_id), None)

def get_comments(article_id):
    return [comment for comment in mock_comments if comment['article_id'] == article_id]

def get_comment_by_id(comment_id):
    return next((comment for comment in mock_comments if comment['id'] == comment_id), None)

def create_article(title, content):
    new_article_id = max(article['id'] for article in mock_articles) + 1
    new_article = {'id': new_article_id, 'title': title, 'content': content}
    mock_articles.append(new_article)
    return new_article

def update_article(article_id, title, content):
    article = get_article_by_id(article_id)
    if article:
        article['title'] = title
        article['content'] = content
        return article
    return None

def delete_article(article_id):
    global mock_articles
    mock_articles = [article for article in mock_articles if article['id'] != article_id]

def create_comment(article_id, content):
    new_comment_id = max(comment['id'] for comment in mock_comments) + 1
    new_comment = {'id': new_comment_id, 'content': content, 'article_id': article_id}
    mock_comments.append(new_comment)
    return new_comment

def update_comment(comment_id, content):
    comment = get_comment_by_id(comment_id)
    if comment:
        comment['content'] = content
        return comment
    return None

def delete_comment(comment_id):
    global mock_comments
    mock_comments = [comment for comment in mock_comments if comment['id'] != comment_id]
