# ✺⭆ : nejauši izvēlēti simboli, lai dators saprastu, kad ir nākamais mainīgais, lasot un rakstot failos (pēc iespējas neiespējamāki, lai nebūtu iespēja, ka parādīsies tekstā)

class Post:
    def __init__(self, id, subreddit, title, content, top_comments):
        self.id = id
        self.subreddit = subreddit.replace("\n", "\\n")
        self.title = title.replace("\n", "\\n")
        self.content = content.replace("\n", "\\n")
        self.top_comments = []


class Comment:
    def __init(self, content):
        self.content = content
        self.parentPost = ""
    

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
                print(f"writing file nr : {i}")
                p = self.list[i]
                f.write(p.id+"✺⭆"+p.subreddit+"✺⭆"+p.title+"✺⭆"+p.content+"✺⭆"+repr(p.top_comments)+"\n")
                
    # ielādēt no faila bet saglabāts tā ka pēdējā līnija ir pirmais elements listā
    def load_from_file(self, filename, line_count):
        self.list = [""]*line_count
        with open(filename, "r", encoding="utf-8") as f:
            i = line_count
            for line in f:
                i -= 1
                p = line.split("✺⭆")
                self.list[i] = Post(p[0], p[1], p[2], p[3], eval(p[4]))
    
    def print(self):
        print(self.list)
        for p in self.list:
            print(p.id + " | r/" + p.subreddit + " | " + p.title[:20] + "... | " + p.content[:50] + "...")