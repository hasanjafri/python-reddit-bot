from praw import Reddit
from time import sleep

class Reddit_Client(object):
    def __init__(self):
        self.reddit_client = Reddit(client_id='-wWMNrpYtVcwWg', client_secret='3Uyzxf4Fll0cAEItawlyoSscdsw', username='toodopestyll', password='dabura45', user_agent="python-reddit-LoS:v0.1 by /u/toodopestyll")
        self.paran_client = Reddit(client_id='-wWMNrpYtVcwWg', client_secret='3Uyzxf4Fll0cAEItawlyoSscdsw', username='LeagueofSavages1', password='21savageha', user_agent="python-reddit-LoS:v0.1 by /u/LeagueofSavages1")

    def print_self(self):
        try:
            return str(self.reddit_client.user.me()) + ' and ' + str(self.paran_client.user.me())
        except Exception as e:
            return("Error! Failed to login to Reddit! Please double check credentials! \n %s" % (e))

    def post_to_subreddit(self, title, url, subreddit, account):
        if not title:
            return "Error! Please provide a title for the post"
        if not url:
            return "Error! Please provide a YouTube URL for sharing"
        if not subreddit:
            return "Error! Please provide the name of the subreddit to make this post on"
        if not account:
            return "Error! Please select the account to share this post with"

        subredditList = [x.strip() for x in subreddit.split(',')]
        new_posts_urls = []            

        if account == 'LeagueofSavages1':
            for subreddit in subredditList:
                try:
                    new_post = self.paran_client.subreddit(subreddit).submit(title=title, url=url)
                except Exception as e:
                    return("Error! Failed to post! \n %s" % (e))
                new_posts_urls.append(str(new_post.permalink))
                sleep(666)
        elif account == 'TooDopeStyll':
            for subreddit in subredditList:
                try:
                    new_post = self.reddit_client.subreddit(subreddit).submit(title=title, url=url)
                except Exception as e:
                    return("Error! Failed to post! \n %s" % (e))
                new_posts_urls.append(str(new_post.permalink))
                sleep(666)
        else:
            return "Error! Invalid account name!"

        return dict(map(reversed, enumerate(new_posts_urls)))
