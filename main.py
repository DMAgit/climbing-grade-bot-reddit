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
re_V = r"^[V,v]([1][0-9]|[0-9])\b"
re_YDS = r"^5.([4-9][^a-z]|1[0-5][a-d]?[^e-z])"  # untested


def v_to_font(grade):
    """
    Convert from V-scale grade to Font grade
    :param grade: String
    :return converted_grade:
    """

    # remove non-alphanumeric characters
    grade = re.sub(r'[^a-zA-Z0-9]', '', grade)
    grade = grade.lower()

    if grade == "v0":
        converted_grade = "4 or 4+"
    elif grade == "v1":
        converted_grade = "5 or 5+"
    elif grade == "v2":
        converted_grade = "6a"
    elif grade == "v3":
        converted_grade = "6a+ or 6b"
    elif grade == "v4":
        converted_grade = "6b+ or 6c"
    elif grade == "v5":
        converted_grade = "6c or 6c+"
    elif grade == "v6":
        converted_grade = "7a"
    elif grade == "v7":
        converted_grade = "7a+"
    elif grade == "v8":
        converted_grade = "7b or 7b+"
    elif grade == "v9":
        converted_grade = "7b+ or 7c"
    elif grade == "v10":
        converted_grade = "7c or 7c+"
    elif grade == "v11":
        converted_grade = "7c+ or 8a"
    elif grade == "v12":
        converted_grade = "8a or 8a+"
    elif grade == "v13":
        converted_grade = "8a+ or 8b"
    elif grade == "v14":
        converted_grade = "8b+"
    elif grade == "v15":
        converted_grade = "8c"
    elif grade == "v16":
        converted_grade = "8c+"
    elif grade == "v17":
        converted_grade = "9a"
    elif grade == "v18":
        converted_grade = "9a+ or 9b"
    elif grade == "v19":
        converted_grade = "9b or 9b+"
    return converted_grade


def YDS_to_french(grade):
    """
    Convert from YDS grade to French sport climbing grade
    :param grade: String
    :return converted_grade:
    """
    pass
    return converted_grade


# for submission in subreddit.stream.submissions():
#     print(submission.title)

for comment in subreddit.stream.comments():
    # we don't want to convert comments we or MountainProjectBot made
    if comment.author != "MountainProjectBot" and comment.author != "climb-grade-bot":
        for word in comment.body.split():
            if re.search(re_V, word):  # check if the word is a V-grade
                v_to_font(word)
            elif re.search(re_YDS, word):  # check if the word is a YDS grade
                YDS_to_french(word)
