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
        postu_sar.add(Post.create(item))

        saved_count += 1

    clear_file(POSTS_FILE)
    
    print("\nLIST 1")
    postu_sar.write_to_file(POSTS_FILE)
    postu_sar.print()
    
    print("\nLIST 2")
    subr_list = ["SideProject", "SoloDevelopment"]
    specific_posts = postu_sar.searchby_subreddit(subr_list)
    specific_posts.print()
    
    print(saved_count)