import praw
from functions.classes import *
# from openai import OpenAI

if __name__ == '__main__':

    reddit = 0
    logged_in = False
    command = [""]
    default_postu_saraksts = PostList()  
                                                                   
    print(" ______   ______   ______   ______   ______   ______")
    print("/_____/  /_____/  /_____/  /_____/  /_____/  /_____/")
    print("\033[1m\33[92m"+"\nSveicināti, reddit saglabāto postu apstrādātājā!"+"\033[0m")
    print("\033[0;36m"+"(Autors: Valdis Arelis 231RMC177 11.grupa)\n"+"\033[0m")
    print("Izmantojiet komandu '"+"\033[1m"+"login"+"\033[0m"+"', lai ielogotos savā reddit profilā!")
    print("Izmantojiet komandu '"+"\033[1m"+"help"+"\033[0m"+"', lai redzētu visas pieejamās komandas!\n")
    
    while command[0] != "exit":
        command = input("\033[1m"+"Komanda: "+"\033[0m").split()
        
        match command[0]:
#HELP-------------------------------------------------------------------------------------------------------------HELP
            case "help":
                print("\033[1m\33[4m"+"\nKomandu saraksts:"+"\033[0m")
                print("\033[1m"+"login <'client_id:client_secret:agent_name:username:password'>"+"\033[0m"+" : ielogoties savā reddit profilā (jābūt uztaisītam 'user agent')")
                print("\033[1m"+"fetch <skaits>"+"\033[0m"+" : ievāc un ielādē noteiktu skaitu saglabāto postu no ielogotā reddit profila un saglabā tos failā posts.txt")
                print("\033[1m"+"load"+"\033[0m"+" : ielādē visus iepriekš saglabātos datus par postiem")
                print("\033[1m"+"print"+"\033[0m"+" : izprintē šobrīd ielādētos postus")
                print("\033[1m"+"search <subreddits[]>"+"\033[0m"+" : meklēt visus saglabātos postus zem šī/-iem subreddit")
                print("\033[1m"+"exit"+"\033[0m"+" : izslēgt programmu")
                print()
#LOGIN------------------------------------------------------------------------------------------------------------LOGIN
            case "login":
                if (len(command) != 2):         # komandas parametru daudzuma pārbaude
                    print("\nFormāts: login <'client_id:client_secret:agent_name:username:password'>\n")
                    continue
                
                input_params = command[1].split(":")
                if len(input_params) != 5:              # login detaļu noformējuma pārbaude
                    print("\nLūdzu tieši 5 parametrus <'client_id:client_secret:agent_name:username:password'>\n")
                    continue
                
                reddit = setup_reddit(input_params)     # ielogojamies reddit, ja kaut kas nav, tad atgriež skaitli
                if (reddit is not int):
                    print("\033[1m\33[92m"+"\nVeiksmīga ielogošanās!\n"+"\033[0m")
                    logged_in = True
                    continue
                elif (reddit == 1):
                    print("\33[91m"+"\nVismaz viens no parametriem nav pareizs\n"+"\033[0m")
                    continue
                else:
                    print("\33[91m"+"\nKaut kas nogāja greizi :(\n"+"\033[0m")
                    continue
#FETCH------------------------------------------------------------------------------------------------------------FETCH
            case "fetch":
                if (len(command) != 2):         # komandas parametru daudzuma pārbaude
                    print("\nFormāts: fetch <skaits>\n")
                    continue
                if (command[1].isnumeric()):        # pārbaude vai dots skaitlis
                    command[1] = int(command[1])
                else:
                    print("\nLūdzu ievadīt int tipa skaitu\n")
                    continue
                if (logged_in != True):         # pārbaude vai lietotājs ir ielogojies
                    print("\nLietotājs nav ielogojies\n")
                    continue
                try:                    # postu ievākšana
                    print("\nIegūstu postus... (Iespējams būs mazliet jāuzgaida)\n")
                    default_postu_saraksts = fetchload_posts(reddit, command[1])
                except:
                    print("\33[91m"+"\nKaut kas nogāja greizi :(\n"+"\033[0m")
                    continue
#LOAD-------------------------------------------------------------------------------------------------------------LOAD
            case "load":
                default_postu_saraksts.load_from_file(POSTS_FILE)
                print("\033[1m\33[92m"+f"\nVeiksmīgi ielādēju {len(default_postu_saraksts.list)} postus no šī faila: "+"\033[0m"+f"{POSTS_FILE}\n")
#PRINT------------------------------------------------------------------------------------------------------------PRINT
            case "print":
                print("\033[1m\33[93m"+f"\nIelādēti ir {len(default_postu_saraksts.list)} posti. Printēju tos!\n"+"\033[0m")
                default_postu_saraksts.print()
                print()
#SEARCH-----------------------------------------------------------------------------------------------------------SEARCH
            case "search":
                if (len(command) < 2):      # komandas parametru daudzuma pārbaude
                    print("\nFormāts: search <subreddits[]>\n")
                    continue
                subreddits = command[1:]    # apstrādājam un izprintējam vaicājumu
                print("\033[1m"+"\nMeklēju"+"\033[0m"+"... ( vaicājums: ", end="")
                for subr in subreddits:
                    print(subr + " ", end="")
                print(")")
                
                results_list = default_postu_saraksts.searchby_subreddit(subreddits)    # atgriežam meklējuma rezultātus
                results_list.print()
#EXIT-------------------------------------------------------------------------------------------------------------EXIT
            case "exit":
                print("\033[1m\33[93m"+"\nSlēdzos ārā! :)"+"\033[0m")
#DEFAULT----------------------------------------------------------------------------------------------------------DEFAULT
            case _:
                print("\nNezināma komanda! Izmanto '"+"\033[1m"+"help"+"\033[0m"+"', lai redzētu visas komandas\n")