# Big-Bang
#Website-FILMTHUSIASTS
#SSL Project
**Tech Stack used:**
Django
Python
SqQLite
HTML
CSS
Bootstrap
JavaScript
Rapid API
**User Functions:**
Search for movies with similar movie suggestions
Add a movie to the already watched list
Add a movie to the to be watched list
Add a movie to the liked list
 **Step 1: Fetch movie details
Details of about 850 movies including:**
Ratings (from all platforms)
Plot
Language 
Similar Movie/ TV Show 
Year of release  
Duration 
Genre
Cast
User reviews 
Platform (where to watch) 
Was fetched from websites like imdb , rotten tomatoes and metacritic . This was done using Rapid api,  the world's largest API hub, which provides us with an api key and using python . The file /data/fetch.py contains the code for the same. The data collected is stored in the file ‘imdb_final4.csv’
**Step 2:**
A model for storing the movie details was made in cinema/members/models.py.The data from the csv file was then stored in a sqlite database in django .

**Step3 :**
A search bar is there on the top right which helps show movie details pertaining to user queries .

**Step 4:**
User authentication was handled using User Creation Form .Login , logout and register features were added.

**Step 5:**
Models for the watchlist(already watched) , to be watched movies  and liked movies was created for the user .




