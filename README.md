# Reddit saglabāto postu apstrādātājs
Autors: Valdis Arelis 231RMC177 11.grupa  
Nepieciešamā bibliotēkas: PRAW, flask (tikai, ja vēlas pamēģināt rādīt datus browserī, priekš main.py šī nav vajadzīga) 

---

##  Vispārējā ideja
Plaši pazīstamajā sociālajā tīklā "Reddit" ir iespēja saglabāt postus. Tas nozīmē, ka tie tiek saistīti ar lietotāja profilu un tiem var piekļūt zem sadaļas "saved".  
Es gadiem lietojot šo sociālo tīklu esmu izmantojis šo funkciju diezgan ekstensīvi, kas nozīmē, ka man ir saglabāti daudz postu (pāri 800). Problēma, tāda, ka "Reddit" nav funkcionalitātes tos kārtot vai meklēt tajos, vai jebkāda cita funkcionalitāte, kas atļautu vieglāk iet tiem cauri vai iegūt informāciju apkopotā veidā. Katrs posts ir jāapskata manuāli.  
Tāpēc radās ideja, ieviest dažādas funkcijas kā tos saglabāt lokāli un spēt apstrādāt kā datu kopu ātri, efektīvi un, galvenais, automātiski.  
  

## Plānotās un implementētās funkcijas

• Ievākt visus saglabātos postus un saglabāt tos kādā failā, lai varētu tos viegli apstrādāt *(paveikts, bet iespējami uzlabojumi)*  
• Spēt ielādēt un apstrādāt iepriekš saglabātos datus pat neielogojoties "Reddit" *(paveikts)*  
• Spēt datus kaut kādā veidā parādīt *(paveikts, bet iespējami uzlabojumi)*  
• Spēt datus parādīt un citādi apstrādāt interneta pārlūkā, tas ir, izveidot lietotāja saskarni ar Flask bibliotēkas palīdzību un html,css,javascript *(daļēji paveikts, bet nav iestrādāts main.py)*  
• Spēt meklēt un filtrēt saglabātos datos pēc dažādiem kritērijiem *(daļēji paveikts)*  
• Spēt katru postu (vai arī pēc izvēles) apkopot/saīsināt (angl. summarize) izmantojot DeepSeek AI *(nav paveikts)*  

## Programmas darbības apraksts
(Lielākai daļai klašu un funkciju, kas atrodamas main.py un classes.py ir pierakstīti komentāri, kas īsumā izskaidro, ko konkrētā klase vai funkcija dara.)  
Programma ir veidota cenšoties ņemt vērā iespējamos nākotnes paplašinājumus.  
Tā ir termināļa programma ar dažādām komandām un komandu argumentiem, lai sasniegtu vēlamos rezultātus un informētu lietotāju:  
![image](https://github.com/user-attachments/assets/2ce07ff0-1bb7-4342-93b4-69792ef727e6)  
Komanda 'help' dod visu komandu aprakstus:  
![image](https://github.com/user-attachments/assets/c21cb48a-5b4b-425c-9575-f1074a3fa6a9)  
Video ar lietošanu:  
https://youtu.be/2ouylo1c-x4

## Funkciju implementāciju detalizēts apraksts

#### Postu ieguve no Reddit  
Izmantota tiek bibliotēka PRAW (Pyhton Reddit API Wrapper). Tā izmanto jau esošo reddit api, kas ļauj iegūt informāciju pa taisno. Gribeju izmantot webscraping metodes (un bibiliotēku requests), bet no sākuma gribējās uztaisīt vienkāršāku variantu ar PRAW un tad, ja laiks atļautu, izveidotu risinājumu ar requests, bet, tam laika nebija. (Šim pašam tika izmantotas ap 50 stundu)  
Lai varētu iegūt datus izmantojot PRAW iekš sava "Reddit" profila ir manuāli jāizveido 'user agent' un tad caur kodu var ielogoties "Reddit" un izmantot visas PRAW funkcijas.  
Kā izveidot user agent un iegūt visas nepieciešamās vērtības, lai ielogotos, ir aprakstīts šeit: https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps  

Kad lietotātjs ir ielogojies tad funkcija iet cauri visiem lietotāja saglabātajiem postiem un komentāriem, sākot no pēdējā saglabātā, līdz sasniedz lietotāja noliktu skaita limitu vai arī apskatīti visi saglabātie posti un komentāri. Programma katram postam izveido jaunu Post klases objektu. Un visi tiek saglabāti iekš PostList klases objekta. Bet katram postam ir arī komentāri, kurus man gribetos saglabāt, tāpēc katram Post objektam, papildus, jau daudziem citiem parametriem, ir arī comments[] parametrs, kas satur Comment klases objektus, kurš katrs satur komentāra saturu.  

Bilde ar datu struktūrām:
![image](https://github.com/user-attachments/assets/9397943c-9825-4e04-9cc3-e509d56a4a48)

#### Rakstīšana failā un lasīšana no faila posts.txt  
Lai saglabātu un nolasītu datus izmantotas funkcijas append_to_file() un load_from_file(). Tās strādā ar failu posts.txt, kur katra līnija ir viens posts. Informācija katrā līnijā tiek atdalīta ar diviem reti sastopamiem unicode rakstzīmēm "✺⭆", ko izmanto abas funkcijas, lai saprastu, kad sākas un beidzas noteikti datu veidi (piem. posta nosaukums un posta saturs). Komentāri tiek saglabāti, kā saraksti ar komentāru saturiem.  
Ievērojama detaļa ir saistībā ar to, kādā virzienā posti tiek rakstīti un lasīti. Tie tiek rakstīti tā, lai posti, kas saglabāti pēdējie ir faila apakšā. Kaut arī PRAW datus iegūst sākot ar pašu pēdējo saglabāto postu. Tā tas tiek darīts, lai nākotnē, iegūstot saglabātos postus būtu iespējams neiet tiem visiem cauri, bet vienkārši pievienot jaunos pašā apakšā, tādējādi ievērojami ietaupot laiku, jo postu iegūšana nav pārāk ātra.  

#### Datu parādīšana
Šobrīd ir implementēta vienkārša print funkcija, kas sekojoši noformatē ielādētos datus.  
![image](https://github.com/user-attachments/assets/57cce701-a1ac-4cde-a0cd-83049d50772e)  

#### Meklēšana starp postiem
Meklēšanas funkcija šobrīd spēj meklēt tikai starp subredditiem, vienkārši izejot tiem cauri un atsevišķā PostList objektā saglabājot postus, kuru subreddita nosaukumā ietilpst kāds no vaicājumiem. Iespējami daudz uzlabojumi.  
![image](https://github.com/user-attachments/assets/0e5625d0-353c-4d27-b727-4ccec241260d)

## Nākotnes iespējas
• Protams, izdarīt visu ieplānoto.
• Padarīt ielogošanos vieglāku.
• Ievērojami uzlabot search iespējas.
• To visu skaisti attēlot interneta pārlūkā izmantojot flask.
