import praw
import json
# from openai import OpenAI


def setup_reddit():
    
    # infinitely asking for input until correct
    correct_input = False
    while correct_input == False:
        input_params = input("Input 5 praw parameters (format = 'c_id:c_secret:agent:user:pass') : ").split(":")
        
        # test if not enough paramaters
        if len(input_params) != 5:
            print("Please provide exactly 5 parameters")
            continue
        
        # setup reddit
        reddit = praw.Reddit(
            client_id= input_params[0],
            client_secret= input_params[1],
            user_agent= input_params[2],
            username= input_params[3],
            password= input_params[4]
        )
        
        # test if params are correct
        try: 
            reddit.user.me()
        except:
            print("Atleast one of the parameters is incorrect")
        correct_input = True
    return reddit

def clear_file(): open("posts.txt", "w").close()

def write_to_file(type, subreddit, title, content, top5comments, url):
    item = {
        'type': type,
        'subreddit': subreddit,
        'title': title,
        'content': content,
        'top_comments': top5comments,
        'url': url,
    }
    with open("posts.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
    f.close()

def load_from_file():
    all_items = []
    with open("posts.txt", "r", encoding="utf-8") as f:
        for line in f:
            all_items.append(json.loads(line))
    return all_items



if __name__ == '__main__':

    reddit = setup_reddit()

    savedCount = 0

    clear_file()
    for item in reddit.user.me().saved(limit=20):
        if isinstance(item, praw.models.Submission):
            write_to_file('post', f"{item.subreddit}", f"{item.title}", f"{item.selftext}", "none for now", f"https://www.reddit.com{item.permalink}")
            # read_from_file()
    
        elif isinstance(item, praw.models.Comment):
            write_to_file('comment', f"{item.subreddit}", f"{item.title}", f"{item.body}", "none for now", f"https://www.reddit.com{item.permalink}")
        
        savedCount += 1

    print(savedCount)