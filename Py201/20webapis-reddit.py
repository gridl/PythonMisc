import praw
#Top 25 storeis on reddit
red = praw.Reddit(user_agent='pyred')
red.get_top()
for i in red.get_top():
    print(i, i.url)

# get sub reddits
python = red.get_subreddit('python')
submissions = python.get_hot(limit=5)
for submission in submissions:
    print(submission)


# get item and URL for required sub

# get sub reddits
python = red.get_subreddit('python')
submissions = python.get_top(limit=15)
for submission in submissions:
    print(submission, submission.url)