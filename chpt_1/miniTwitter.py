'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

# Pull Model
class MiniTwitter:

    def __init__(self):
        # do intialization if necessary
        self.globalTweetId = 0
        # tweet table -- (key: user_id, val: array((tweet_id, tweet)) )
        self.tweet_table = {}
        # friends table -- (key: from_user_id, val: array(to_user_id) )
        self.friends_table = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        tweet = Tweet.create(user_id, tweet_text)
        # auto-incr id for newly created tweet
        self.globalTweetId += 1
        if user_id in self.tweet_table:
            # insert into tweet_table using user_id as key (shardingkey)
            # append a tuple of tweet id and tweet object
            self.tweet_table[user_id].append((self.globalTweetId, tweet))
        else:
            self.tweet_table[user_id] = [(self.globalTweetId, tweet)]

        return tweet
    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        # get all user follows
        rt = []
        if user_id in self.tweet_table:
            rt = self.tweet_table[user_id][-10:]

        if user_id in self.friends_table:
            for friend in self.friends_table[user_id]:
                if friend in self.tweet_table:
                    rt.extend(self.tweet_table[friend][-10:])

        def keyFunc(tweet):
            return tweet[0]

        rt.sort(key = keyFunc)
        return [twt[1] for twt in rt[-10:][::-1]]
    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        if user_id in self.tweet_table:
            #if has tweet
            #[-10:] last 10 tweets
            #[::-1] get it in reversed order, one by one
            return [tweet[1] for tweet in self.tweet_table[user_id][-10:][::-1]]
        else:
            #if not found in tweet table no tweet yet
            return []
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        # use set to contain friends to headle duplicates
        if from_user_id not in self.friends_table:
            self.friends_table[from_user_id] = set()
        self.friends_table[from_user_id].add(to_user_id)
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        # if can do unfollow should have had record in friends_table
        # for safety do a check
        if from_user_id not in self.friends_table:
            return
        self.friends_table[from_user_id].remove(to_user_id)


# Push Model
# Did not pass OJ
class MiniTwitter:

    def __init__(self):
        # do intialization if necessary
        # push model
        self.globalTweetId = 0
        self.tweet_table = {}
        self.news_feed_table = {}
        self.friends_table = {} # key from_user : to_user: lookup who keyusers follow
        self.follower_table = {} # key to_user : from_user: lookpu keyusers follower (for fanout process)

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        # 1. write in tweet_table
        # 2. then fanout in news_feed_table

        tweet = new Tweet(user_id, tweet_text)
        self.globalTweetId += 1
        # 1.
        if user_id in self.tweet_table:
            self.tweet_table[user_id].append((self.globalTweetId, tweet))
        else:
            tweet_table[user_id] = [(self.globalTweetId, tweet)]

        # 2. fanout
        if user_id in self.follower_table:
            for follower in self.follower_table[user_id]:
                if follower in self.news_feed_table:
                    self.news_feed_table[follower].apppend(self.globalTweetId)
                else:
                    self.news_feed_table[follower] = [self.globalTweetId]

        return tweet
    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        # read from news_feed_table directly
        if user_id in self.news_feed_table:
            return [self.tweet_table[id] for id in self.news_feed_table[user_id][-10:][::-1]]
        else:
            return []
    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        # read from tweet_table directly
        if user_id in tweet_table:
            return [tweet[1] for tweet in self.tweet_table[user_id][-10:][::-1]]
        else:
            return []
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.friends_table:
            self.friends_table[from_user_id] = set()
        self.friends_table[from_user_id].append(to_user_id)

        if to_user_id not in self.follower_table:
            self.follower_table[to_user_id] = set()
        self.follower_table[to_user_id].append(from_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.friends_table:
            return
        self.friend_table[from_user_id].remove(to_user_id)

        if to_user_id not in self.follower_table:
            return
        self.follower_table[to_user_id].remove(from_user_id)
