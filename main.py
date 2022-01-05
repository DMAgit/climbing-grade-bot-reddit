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
re_V = r"^[V,v]([1][0-9]|[0-9])\b"  # seems to work
re_YDS = r"^5.([4-9][^a-z]|1[0-5][a-d]?[^e-z])"  # seems to work


def v_to_font(grade):
    """
    Convert from V-scale grade to Font grade
    :param grade: String
    :return converted_grade:
    """

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

    else:
        return "No conversion found (something went wrong). calling for /u/PM_ME_YOUR_PROFANITY"

    return converted_grade


def YDS_to_french(grade):
    """
    Convert from YDS grade to French sport climbing grade
    :param grade: String
    :return converted_grade:
    """

    if grade == "5.4":
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
    elif grade == "5.10a":
        converted_grade = "6a"
    elif grade == "5.10b":
        converted_grade = "6a+"
    elif grade == "5.10c":
        converted_grade = "6a+"
    elif grade == "5.10d":
        converted_grade = "6b"
    elif grade == "5.11a":
        converted_grade = "6b+"
    elif grade == "5.11b":
        converted_grade = "6c"
    elif grade == "5.11c":
        converted_grade = "6c+"
    elif grade == "5.11d":
        converted_grade = "7a"
    elif grade == "5.12a":
        converted_grade = "7a+"
    elif grade == "5.12b":
        converted_grade = "7b"
    elif grade == "5.12c":
        converted_grade = "7b+"
    elif grade == "5.12d":
        converted_grade = "7c"
    elif grade == "5.13a":
        converted_grade = "7c+"
    elif grade == "5.13b":
        converted_grade = "8a"
    elif grade == "5.13c":
        converted_grade = "8a+"
    elif grade == "5.13d":
        converted_grade = "8b"
    elif grade == "5.14a":
        converted_grade = "8b+"
    elif grade == "5.14b":
        converted_grade = "8c"
    elif grade == "5.14c":
        converted_grade = "8c+"
    elif grade == "5.14d":
        converted_grade = "9a"
    elif grade == "5.15a":
        converted_grade = "9a+"
    elif grade == "5.15b":
        converted_grade = "9b"
    elif grade == "5.15c":
        converted_grade = "9b+"
    elif grade == "5.15d":
        converted_grade = "9c"

    else:
        return "No conversion found (something went wrong). Calling for /u/PM_ME_YOUR_PROFANITY"

    return converted_grade


def build_comment(grade, converted_grade):
    return f"A **{grade}** is a(n) **{converted_grade}**.\n\n"


# for submission in subreddit.stream.submissions():
#     print(submission.title)

for comment in subreddit.stream.comments():
    # we don't want to convert comments we or MountainProjectBot made
    if comment.author != "MountainProjectBot" and comment.author != "climb-grade-bot":
        for string in comment.body.split():
            word_list = string.split("/")  # sometimes people will write grade1/grade2
            # this would be passed as one word and get through the RegEx filter and break everything,
            # so we check for that case and split on "/" (if there is one, if not it's a list of one word)
            for word in word_list:
                if re.search(re_V, word):  # check if the word is a V-grade
                    grade_old = re.sub(r'[^a-zA-Z0-9]', '', word).upper()
                    grade_new = v_to_font(grade_old)
                    print(build_comment(grade_old, grade_new))
                elif re.search(re_YDS, word):  # check if the word is a YDS grade
                    grade_old = re.sub(r"^\W+|\W+$", "", word).lower()
                    grade_new = YDS_to_french(grade_old)
                    print(build_comment(grade_old, grade_new))

