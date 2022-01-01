import praw
import config

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)

# print(reddit.read_only)
target_sub = "climbing+bouldering+climbharder"
subreddit = reddit.subreddit(target_sub)


def posts():
    pass
    for submission in subreddit.stream.submissions():
        print(submission.title)


def comments():
    pass
    for comment in subreddit.stream.comments():
        print(comment.body)
