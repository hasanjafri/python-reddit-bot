from flask import Flask, request, render_template
import logging
from reddit_client import Reddit_Client

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='./app.log', filemode='w')

application = Flask(__name__)

reddit_bot_client = Reddit_Client()

@application.route('/')
def test_server_online():
    return "Server is online"

@application.route('/me')
def print_logged_user():
    return reddit_bot_client.print_self()

@application.route('/post', methods=['GET', 'POST'])
def post_to_subreddit():
    error = None
    response = None
    if request.method == 'POST':
        if 'title' not in request.form:
            error = "No title provided for the post to share"
        if 'subreddit' not in request.form:
            error = "No subreddit provided to post this to"
        if 'url' not in request.form:
            error = "No url provided to share in this post"
        if 'account' not in request.form:
            error = "No account selected to share this post with"

        title = request.form.get('title')
        url = request.form.get('url')
        subreddit = request.form.get('subreddit')
        account = request.form.get('account')

        res = reddit_bot_client.post_to_subreddit(title, url, subreddit, account)
        if isinstance(res, dict):
            response = res
        else:
            error = res
        
    return render_template('post.html', error=error, response=response)

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=8080)