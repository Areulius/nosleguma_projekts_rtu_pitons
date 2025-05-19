# Reddit saglabāto postu apstrādātājs
Autors: Valdis Arelis 231RMC177 11.grupa  

---

##  Vispārējā ideja
Plaši pazīstamajā sociālajā tīklā "Reddit" ir iespēja saglabāt postus. Tas nozīmē, ka tie tiek saistīti ar lietotāja profilu un tiem var piekļūt zem sadaļas "saved".  
Es gadiem lietojot šo sociālo tīklu esmu izmantojis šo funkciju diezgan ekstensīvi, kas nozīmē, ka man ir saglabāti daudz postu (pāri 800). Problēma, tāda, ka "Reddit" nav funkcionalitātes tos kārtot vai meklēt tajos, vai jebkāda cita funkcionalitāte, kas atļautu vieglāk iet tiem cauri vai iegūt informāciju apkopotā veidā. Katrs posts ir jāapskata manuāli.  
Tāpēc radās ideja, ieviest dažādas funkcijas kā tos saglabāt lokāli un spēt apstrādāt kā datu kopu ātri, efektīvi un, galvenais, automātiski.  
  

### Plānotās un implementētās funkcijas

• Ievākt visus saglabātos postus un saglabāt tos kādā failā, lai varētu tos viegli apstrādāt *(paveikts)*
• Spēt ielādēt un apstrādāt iepriekš saglabātos datus pat neielogojoties "Reddit" *(paveikts)*
• Spēt datus kaut kādā veidā parādīt *(paveikts)*
• Spēt datus parādīt un citādi apstrādāt interneta pārlūkā, tas ir, izveidot lietotāja saskarni ar Flask bibliotēkas palīdzību un html,css,javascript *(daļēji paveikts, bet nav iestrādāts main.py)*
• Spēt meklēt un filtrēt saglabātos datos pēc dažādiem kritērijiem *(daļēji paveikts)*
• Spēt katru postu (vai arī pēc izvēles) apkopot/saīsināt (angl. summarize) izmantojot DeepSeek AI *(nav paveikts)*

### Programmas darbības apraksts
(Lielākai daļai klašu un funkciju, kas atrodamas main.py un classes.py ir pierakstīti komentāri, kas īsumā izskaidro, ko konkrētā klase vai funkcija dara.)  
Programma ir veidota cenšoties ņemt vērā iespējamos nākotnes paplašinājumus. Tā ir termināļa programma ar dažādām komandām un komandu argumentiem, lai sasniegtu vēlamos rezultātus un informētu lietotāju.  
Komanda 'help' dod visu komandu aprakstus.

### Funkciju implementāciju detalizēts apraksts


#### Postu ieguve no Reddit

#### Rakstīšana failā un lasīšana no faila posts.txt

#### Datu parādīšana

#### Meklēšana starp postiem

### Nākotnes iespējas