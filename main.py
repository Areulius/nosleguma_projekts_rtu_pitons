import praw
from functions.functions import *
from functions.classes import *
# from openai import OpenAI


# konstantes
POSTS_FILE = "txt_files/posts.txt"
COMMENTS_FILE = "txt_files/comments.txt"

if __name__ == '__main__':

    reddit = setup_reddit()

    savedCount = 0

    post_listt = PostList()
    for item in reddit.user.me().saved(limit=5):
        if isinstance(item, praw.models.Submission):
            # write_to_file('post', f"{item.subreddit}", f"{item.title}", f"{item.selftext}", "none for now", f"https://redd.it/{item.id}")
            
            post_listt.add(Post(f"{item.id}", f"{item.subreddit}", f"{item.title}", f"{item.selftext}", ""))
    
        elif isinstance(item, praw.models.Comment):
            # write_to_file('comment', f"{item.subreddit}", None, f"{item.body}", None, f"https://www.reddit.com{item.permalink}")
            print("comment")
        
        savedCount += 1

    clear_file(POSTS_FILE)
    post_listt.write_to_file(POSTS_FILE)
    print("PRINTING LIST 1\n\n")
    post_listt.print()
    
    list2 = PostList()
    list2.load_from_file(POSTS_FILE, post_listt.post_count)
    list2.write_to_file(POSTS_FILE)
    print("PRINTING LIST 2\n\n")
    list2.print()
    
    print(savedCount)