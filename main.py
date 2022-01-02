import praw
import config
import re

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

# RegEx
re_V = "^[V,v]([1][0-9]|[0-9])\b"
re_YDS = ""

# for submission in subreddit.stream.submissions():
#     print(submission.title)

for comment in subreddit.stream.comments():
    # we don't want to convert comments we or MountainProjectBot made
    if not comment.author == "MountainProjectBot" or "climb-grade-bot":
        for word in comment.body.split():
            if re.search(re_V, word):  # check if the word is a V-grade
                pass
            elif re.search(re_YDS, word):  # check if the word is a YDS grade
                pass


def v_to_french(grade):
    """
    Convert from V-grade to French boulder grade
    :param grade: String
    :return converted_grade:
    """
    pass
    return converted_grade


def YDS_to_french(grade):
    """
    Convert from YDS grade to French sport climbing grade
    :param grade: String
    :return converted_grade:
    """
    pass
    return converted_grade
