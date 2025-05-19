import praw
# ✺⭆ : nejauši izvēlēti simboli, lai dators saprastu, kad ir nākamais mainīgais, lasot un rakstot failos (pēc iespējas neiespējamāki, lai nebūtu iespēja, ka parādīsies tekstā)

#konstantes
FETCHED_COMMENT_COUNT = 3

def setup_reddit():

    # infinitely asking for input until correct
    correct_input = False
    while correct_input == False:
        input_params = input("Login with praw parameters (format = 'c_id:c_secret:agent:user:pass') : ").split(":")

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

class Comment:
    def __init__(self, content):
        self.content = content

def fetch_top_comments(item):
    fetched_comments = []
    item.comment_limit = FETCHED_COMMENT_COUNT
    item.comments.replace_more(limit=0)
    
    com_count = len(item.comments)
    n = FETCHED_COMMENT_COUNT
    if (com_count < n):
        n = com_count
    
    for i in range(n):
        body = item.comments[i].body
        if body not in ("[deleted]", "[removed]"):
            fetched_comments.append(Comment(body))
    return fetched_comments

class Post:
    def __init__(self, id, subreddit, title, content, top_comments: Comment):
        self.id = id
        self.subreddit = subreddit.replace("\n", "\\n")
        self.title = title.replace("\n", "\\n")
        self.content = content.replace("\n", "\\n")
        self.top_comments = top_comments
    
    def create(item):
        top_comments = fetch_top_comments(item)
        return Post(f"{item.id}", f"{item.subreddit}", f"{item.title}", f"{item.selftext}", top_comments)
    
class PostList:
    def __init__(self):
        self.list = []
        self.post_count = 0

    def add(self, new_post):
        self.list.append(new_post)
        self.post_count += 1
    
    # rakstīt failā bet 'in reverse', lai nebūtu visi jāpārliek par vienu rindiņu uz priekšu, kad seivo jaunus postus (saglabā O(1), kad jāpievieno jauni saglabāti posti)
    def write_to_file(self, filename):
        with open(filename, "a", encoding="utf-8") as f:
            for i in range(self.post_count-1, -1, -1): # for loop atpakaļgaitā, sākot no pēdējā posta
                p = self.list[i]
                
                com_list = []
                for comment in p.top_comments:
                    com_list.append(comment.content)
                    
                f.write(p.id+"✺⭆"+p.subreddit+"✺⭆"+p.title+"✺⭆"+p.content+"✺⭆"+repr(com_list)+"\n")
                
    # ielādēt no faila bet saglabāts tā ka pēdējā līnija ir pirmais elements listā
    def load_from_file(self, filename, line_count):
        self.list = [""]*line_count
        with open(filename, "r", encoding="utf-8") as f:
            i = line_count
            for line in f:
                i -= 1
                p = line.split("✺⭆")
                
                Comment_list = []
                for comment_text in eval(p[4]):
                    Comment_list.append(Comment(comment_text))
                self.list[i] = Post(p[0], p[1], p[2], p[3], Comment_list)
    
    def print(self):
        for p in self.list:
            com_list = []
            for comment in p.top_comments:
                com_list.append(comment.content)
            print(p.id + " | r/" + p.subreddit + " | " + p.title[:20] + "... | " + p.content[:50] + "... | " + repr(com_list))