from praw import Reddit

class Reddit_Client(object):
    def __init__(self):
        self.reddit_client = Reddit(client_id='-wWMNrpYtVcwWg', client_secret='3Uyzxf4Fll0cAEItawlyoSscdsw', username='toodopestyll', password='dabura45', user_agent="python-reddit-LoS:v0.1 by /u/toodopestyll")

    def print_self(self):
        try:
            return str(self.reddit_client.user.me())
        except Exception as e:
            return("Error! Failed to login to Reddit! Please double check credentials! \n %s" % (e))

    def post_to_subreddit(self, title, url, subreddit):
        if not title:
            return "Error! Please provide a title for the post"
        if not url:
            return "Error! Please provide a YouTube URL for sharing"
        if not subreddit:
            return "Error! Please provide the name of the subreddit to make this post on"

        try:
            new_post = self.reddit_client.subreddit(subreddit).submit(title=title, url=url)
        except Exception as e:
            return("Error! Failed to post! \n %s" % (e))

        return {"url": str(new_post.permalink)}
