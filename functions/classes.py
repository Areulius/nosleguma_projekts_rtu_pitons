# autors Valdis Arelis 231RMC177

import praw
# ✺⭆ : nejauši izvēlēti simboli, lai dators saprastu, kad ir nākamais mainīgais, lasot un rakstot failos (pēc iespējas neiespējamāki, lai nebūtu iespēja, ka parādīsies tekstā)

#konstantes
FETCHED_COMMENT_COUNT = 3
POSTS_FILE = "txt_files/posts.txt"

# ielogošanās reddit profilā
def setup_reddit(input_params):

    reddit = praw.Reddit(
        client_id= input_params[0],
        client_secret= input_params[1],
        user_agent= input_params[2],
        username= input_params[3],
        password= input_params[4]
    )
        
    # pārbaude vai parametri ir pareizi
    try: 
        reddit.user.me()
    except:
        return 1
        
    return reddit

def clear_file(filename): open(filename, "w").close()

# izskaita līnijas failā
def count_lines(filename):
    line_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
    return line_count

# komentāra klases objekts, izveidots, lai nākotnē būtu vieglāk darboties ar komentāriem dziļāk
class Comment:
    def __init__(self, content):
        self.content = content

# iegūt specifiska posta visaugstāk novērtētos komentārus, nesaglabā, ja komentārs ir izdzēsts, komentāru skaits atkarīgs no FETCHED_COMMENT_COUNT
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

# Post klases objekts ar visu man noderīgo info, ko satur specifisks posts
class Post:
    def __init__(self, id, subreddit, title, content, top_comments: Comment):
        self.id = id
        self.subreddit = subreddit.replace("\n", "\\n")
        self.title = title.replace("\n", "\\n")
        self.content = content.replace("\n", "\\n")
        self.top_comments = top_comments
    
    # radīt jaunu Post klases objektu izmantojot praw, kurš iegūst info no reddit API
    def create(item):
        top_comments = fetch_top_comments(item)
        return Post(f"{item.id}", f"{item.subreddit}", f"{item.title}", f"{item.selftext}", top_comments)

# Postu saraksta objekts, satur sarakstu ar Post klases objektiem un dažādas noderīgas funkcijas
class PostList:
    def __init__(self):
        self.list = []
        self.post_count = 0

    # pievienot jaunu postu postu sarakstā
    def add(self, new_post: Post):
        self.list.append(new_post)
        self.post_count += 1
    
    # rakstīt failā bet 'in reverse', lai nebūtu visi jāpārliek par vienu rindiņu uz priekšu, kad seivo jaunus postus (saglabā O(1), kad jāpievieno jauni saglabāti posti)
    def append_to_file(self, filename):
        with open(filename, "a", encoding="utf-8") as f:
            for i in range(self.post_count-1, -1, -1): # for loop atpakaļgaitā, sākot no pēdējā posta
                p = self.list[i]
                
                com_list = []
                for comment in p.top_comments:
                    com_list.append(comment.content)
                    
                f.write(p.id+"✺⭆"+p.subreddit+"✺⭆"+p.title+"✺⭆"+p.content+"✺⭆"+repr(com_list)+"\n")
                
    # ielādēt no faila bet saglabāts tā ka pēdējā līnija ir pirmais elements listā, tāpēc pirmo elementu saglabā pēdējajā lista indeksā
    def load_from_file(self, filename):
        line_count = count_lines(POSTS_FILE)
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
    
    # search by subreddit
    def searchby_subreddit(self, subreddits):
        new_postlist = PostList()
        found_count = 0
        for subr in subreddits:
            subr = subr.lower()
        for post in self.list:
            for subr in subreddits:
                if (post.subreddit.lower().find(subr) != -1):
                    new_postlist.add(post)
                    found_count += 1
        print("\033[1m\33[92m"+f"Atradu {found_count} postus!\n"+"\033[0m")
        return new_postlist
    
    #print all posts from list in a formatted way
    def print(self):
        for p in self.list:
            com_list = []
            for comment in p.top_comments:
                com_list.append(comment.content)
            print(f"http://redd.it/{p.id}".ljust(23) + " | r/" + p.subreddit.ljust(22) + " | " + f"{p.title[:20]}...".ljust(24) + " | " + f"{p.content[:50]}...".ljust(54) + " \t| " + f"({len(com_list)} comments)")

# ievākt saglabātos postus no lietotāja reddit profila un saglabāt tos postu failā
def fetchload_posts(reddit, amount: int):
    saved_count = 0    
    postu_sar = PostList()
    for item in reddit.user.me().saved(limit=amount):
        
        if isinstance(item, praw.models.Comment): # ja saglabāts ir komentārs, tad fokuss tiek mainīts uz postu virs komentāra
            item = reddit.submission(item.link_id[3:])
        postu_sar.add(Post.create(item))

        saved_count += 1
        if (saved_count % 10 == 0):
            print(f"Esmu ieguvis {saved_count} postus. Turpinu...")
            
    clear_file(POSTS_FILE)
    postu_sar.append_to_file(POSTS_FILE)
    
    print("\033[1m\33[92m"+f"\nIeguvu un saglabāju {saved_count} postus kopumā!\n"+"\033[0m")
    return postu_sar