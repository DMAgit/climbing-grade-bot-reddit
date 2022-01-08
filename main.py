import praw
import config  # private info for the reddit API
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
re_V = re.compile(r"^[V,v]([1][0-9]|[0-9])\b")  # seems to work
re_YDS = re.compile(r"^5.([4-9][^a-z]|1[0-5][a-d]?[^e-z])")  # seems to work


def convert(grade):
    """
    Convert from V-scale grade to Font grade or
    YDS to French
    :param grade: String
    :return converted_grade:
    """

    grade = grade.upper()

    if grade == "V0":
        converted_grade = "4 or 4+"
    elif grade == "V1":
        converted_grade = "5 or 5+"
    elif grade == "V2":
        converted_grade = "6a"
    elif grade == "V3":
        converted_grade = "6a+ or 6b"
    elif grade == "V4":
        converted_grade = "6b+ or 6c"
    elif grade == "V5":
        converted_grade = "6c or 6c+"
    elif grade == "V6":
        converted_grade = "7a"
    elif grade == "V7":
        converted_grade = "7a+"
    elif grade == "V8":
        converted_grade = "7b or 7b+"
    elif grade == "V9":
        converted_grade = "7b+ or 7c"
    elif grade == "V10":
        converted_grade = "7c or 7c+"
    elif grade == "V11":
        converted_grade = "7c+ or 8a"
    elif grade == "V12":
        converted_grade = "8a or 8a+"
    elif grade == "V13":
        converted_grade = "8a+ or 8b"
    elif grade == "V14":
        converted_grade = "8b+"
    elif grade == "V15":
        converted_grade = "8c"
    elif grade == "V16":
        converted_grade = "8c+"
    elif grade == "V17":
        converted_grade = "9a"
    elif grade == "V18":
        converted_grade = "9a+ or 9b"
    elif grade == "V19":
        converted_grade = "9b or 9b+"

    elif grade == "5.4":
        converted_grade = "4a"
    elif grade == "5.5":
        converted_grade = "4b"
    elif grade == "5.6":
        converted_grade = "4c"
    elif grade == "5.7":
        converted_grade = "5a"
    elif grade == "5.8":
        converted_grade = "5b"
    elif grade == "5.9":
        converted_grade = "5c"
    elif grade == "5.10A":
        converted_grade = "6a"
    elif grade == "5.10B":
        converted_grade = "6a+"
    elif grade == "5.10C":
        converted_grade = "6a+"
    elif grade == "5.10D":
        converted_grade = "6b"
    elif grade == "5.11A":
        converted_grade = "6b+"
    elif grade == "5.11B":
        converted_grade = "6c"
    elif grade == "5.11C":
        converted_grade = "6c+"
    elif grade == "5.11D":
        converted_grade = "7a"
    elif grade == "5.12A":
        converted_grade = "7a+"
    elif grade == "5.12B":
        converted_grade = "7b"
    elif grade == "5.12C":
        converted_grade = "7b+"
    elif grade == "5.12D":
        converted_grade = "7c"
    elif grade == "5.13A":
        converted_grade = "7c+"
    elif grade == "5.13B":
        converted_grade = "8a"
    elif grade == "5.13C":
        converted_grade = "8a+"
    elif grade == "5.13D":
        converted_grade = "8b"
    elif grade == "5.14A":
        converted_grade = "8b+"
    elif grade == "5.14B":
        converted_grade = "8c"
    elif grade == "5.14C":
        converted_grade = "8c+"
    elif grade == "5.14D":
        converted_grade = "9a"
    elif grade == "5.15A":
        converted_grade = "9a+"
    elif grade == "5.15B":
        converted_grade = "9b"
    elif grade == "5.15C":
        converted_grade = "9b+"
    elif grade == "5.15D":
        converted_grade = "9c"

    else:
        return "No conversion found (something went wrong). calling for /u/PM_ME_YOUR_PROFANITY"

    return converted_grade


# for submission in subreddit.stream.submissions():
#     print(submission.title)

for comment in subreddit.stream.comments():
    if comment.author != "MountainProjectBot" and comment.author != "climb-grade-bot":
        grade_list = [word for word in re.split("[, \-!?:/]+", comment.body)
                      if re_V.search(word) or re_YDS.search(word)]
        reply = '\n\n'.join(f'A {grade} is a(n) {convert(grade)}.' for grade in grade_list)
        if reply:
            print(reply)
