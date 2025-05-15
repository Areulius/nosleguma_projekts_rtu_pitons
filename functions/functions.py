import praw
import json

POSTS_FILE = "txt_files/posts.txt"
COMMENTS_FILE = "txt_files/comments.txt"


# setup praw to have access to reddit api by asking for user to input all needed info
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

def clear_file(filename): open(filename, "w").close()

# convert each submission into a dictionary object and then append it to text file in a json format, each object is on a new line
def write_to_file(type, subreddit, title, content, top5comments, url):
    item = {
        'type': type,
        'subreddit': subreddit,
        'title': title,
        'content': content, #.replace("\n", "<br>")
        'top_comments': top5comments,
        'url': url,
    }
    
    filename = ""
    if type == "post":
        filename = POSTS_FILE
    elif type == "comment":
        filename = COMMENTS_FILE
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# load each object into an all_items list from "posts.txt"
def load_from_file(filename):

    all_items = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            all_items.append(json.loads(line))
    return all_items