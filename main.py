import praw
from functions.functions import *
# from openai import OpenAI

if __name__ == '__main__':

    reddit = setup_reddit()

    savedCount = 0

    clear_file()
    for item in reddit.user.me().saved(limit=30):
        if isinstance(item, praw.models.Submission):
            write_to_file('post', f"{item.subreddit}", f"{item.title}", f"{item.selftext}", "none for now", f"https://redd.it/{item.id}")
            # read_from_file()
    
        elif isinstance(item, praw.models.Comment):
            write_to_file('comment', f"{item.subreddit}", None, f"{item.body}", None, f"https://www.reddit.com{item.permalink}")
            print("comment")
        
        savedCount += 1

    print(savedCount)