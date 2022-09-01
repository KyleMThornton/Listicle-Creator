from os import remove
import praw
import config

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
)

subreddit = reddit.subreddit("askreddit")

for submission in subreddit.hot(limit=1):
    print("This week, Reddit user u/", submission.author, "posed the question,",submission.title,"and there were so many interesting responses! Here are some of the top-voted answers:")
    #print(submission.title)
    #print(submission.score)
    #print(submission.id)
    #print(submission.url)
    submission.comment_sort = "top"
    top_level_comments = list(submission.comments)
    x = 0

    def removeEdits(comment):
        if "Edit" in comment:
            comment = comment.split("Edit", 1)[0]
            return comment
        else:
            return comment


    while x < 10:
        z = removeEdits(top_level_comments[x].body)
        print(x+1,". ",z)
        print("-u/",top_level_comments[x].author)
        x+=1