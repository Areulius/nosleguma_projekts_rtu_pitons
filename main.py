import praw
from functions.classes import *
# from openai import OpenAI

# konstantes
POSTS_FILE = "txt_files/posts.txt"
COMMENTS_FILE = "txt_files/comments.txt"

if __name__ == '__main__':

    reddit = setup_reddit()
    saved_count = 0
    command = [""]
    
    # while command[0] != "exit":
    #     command = input("Command: ").split()
        
    #     match command[0]:
    #         case "print":
    #             print("print case")
    #         case "exit":
    #             print("Exiting! :)")
    #         case _:
    #             print("default case")
           
    # iet cauri visiem lietotāja saglabātajiem postiem un komentāriem un saglabāt tos sarakstā     
    postu_sar = PostList()
    for item in reddit.user.me().saved(limit=3):
        
        if isinstance(item, praw.models.Comment): # ja saglabāts ir komentārs, tad fokuss tiek mainīts uz postu virs komentāra
            print("COMMENT")
            item = reddit.submission(item.link_id[3:])
            # item = item.submission
        print(type(item))
        postu_sar.add(Post.create(item))
        
        


        saved_count += 1

    clear_file(POSTS_FILE)
    postu_sar.write_to_file(POSTS_FILE)
    print("PRINTING LIST 1\n")
    postu_sar.print()
    
    postu_sar2 = PostList()
    postu_sar.load_from_file(POSTS_FILE, postu_sar.post_count)
    print("PRINTING LIST 2\n")
    postu_sar2.print()
    
    print(saved_count)