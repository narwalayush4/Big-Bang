import requests
import pandas as pd
import csv

csvfile=pd.read_csv('imdb_top_250_movies.csv' , encoding ='cp1252')

names = csvfile["newtitle"]


url = "https://imdb8.p.rapidapi.com/auto-complete"
url_review = "https://imdb8.p.rapidapi.com/title/get-user-reviews"
url_genre = "https://imdb8.p.rapidapi.com/title/get-genres"
url_plot = "https://imdb8.p.rapidapi.com/title/get-plots"
url_time = "https://imdb8.p.rapidapi.com/title/find"
url_meta = "https://imdb8.p.rapidapi.com/title/get-meta-data"
url_same = 'https://imdb8.p.rapidapi.com/title/get-more-like-this'

headers = {
	"X-RapidAPI-Key": "2af154bb4fmsh4245423d0c5edc8p129491jsn3bf241c11d5f",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

listing=[]

for i in range(901,975):
    try:
        print(names[i])
    
        querystring = {"q":names[i]}
        response = requests.request("GET", url, headers=headers, params = querystring)
        myjson=response.json()
       
        
        for x in myjson['d']:
        
            movie_id = {"tconst":x['id']}
            moviename={"q":x['l']}
            meta = {"ids":x['id'],"region":"US"}
            same= {'tconst': x['id'], 'currentCountry': 'US', 'purchaseCountry': 'US'}
            response_review = requests.request("GET", url_review, headers=headers, params = movie_id)
            myjson_review=response_review.json()
            response_genre = requests.request("GET", url_genre, headers=headers, params = movie_id)
            myjson_genre=response_genre.json()
            response_plots = requests.request("GET", url_plot, headers=headers, params = movie_id)
            myjson_plots=response_plots.json()
            response_time = requests.request("GET", url_time, headers=headers, params = moviename)
            myjson_time=response_time.json()
            response_meta = requests.request("GET", url_meta, headers=headers, params = meta)
            myjson_meta=response_meta.json()
            response_same = requests.request("GET", url_same, headers=headers, params = same)
            myjson_same=response_same.json()
            count=1
            rev1=''
            revrate1=0
            rev2=''
            revrate2=0
            rev2=''
            revrate2=0
            rev2=''
            revrate2=0
            rev3=''
            revrate3=0
            rev4=''
            revrate4=0
            if 'reviews' in  myjson_review.keys():
                for rev in myjson_review['reviews']:
                    if count ==1 :
                        rev1 = rev['reviewTitle']
                        revrate1=rev['authorRating']
                        count =count+1
                    elif count ==2 :
                        rev2 = rev['reviewTitle']
                        if 'authorRating' in  rev.keys():
                            revrate2=rev['authorRating']
                        count= count+1
                    elif count ==3 :
                        rev3 = rev['reviewTitle']
                        if 'authorRating' in  rev.keys():
                            revrate3=rev['authorRating']
                        count= count+1
                    elif count ==4 :
                        rev4 = rev['reviewTitle']
                        if 'authorRating' in  rev.keys():
                            revrate4=rev['authorRating']
                        count= count+1

                    else :
                        break
            
            list_gen=[]
            for gen in myjson_genre:
                list_gen.append(gen)
            
            plot=""
            if 'plots' in myjson_plots.keys():
                for plt in  myjson_plots['plots']:
                    plot = plt['text']
                    break
            
            dur=0
            for time in myjson_time['results']:
                if 'runningTimeInMinutes' in time.keys():
                    dur = time['runningTimeInMinutes']
                break
            
            rat=0
            platform=''
            if 'ratings' in myjson_meta[x['id']] :
                    if ('userScore' in myjson_meta[x['id']]['metacritic'].keys()):
                        rat=myjson_meta[x['id']]['metacritic']['userScore']
                    if 'optionsGroups' in myjson_meta[x['id']]['waysToWatch'].keys():
                        for temp in myjson_meta[x['id']]['waysToWatch']['optionGroups'][0]['watchOptions']:
                            platform=temp['primaryText']

            same_list=[]
            for same_mov in myjson_same:
                same_list.append(same_mov)


            if 'y' in x.keys():
                year =x['y']
            else :
                year =0

            data = {"movie_title": x['l'],
                    "movie_id": x['id'],
                    "poster": x['i']['imageUrl'],
                    "year": year,
                    "star_cast": x['s'],
                    "rev1": rev1,
                    "revrate1": revrate1,
                    "rev2": rev2,
                    "revrate2": revrate2,
                    "rev3": rev3,
                    "revrate3": revrate3,
                    "rev4": rev4,
                    "revrate4": revrate4,
                    "genre":list_gen,
                    "plot": plot,
                    "duration": dur,
                    "rating" : rat,
                    "platform": platform,
                    "similar" : same_list
                    }
            listing.append(data)
            break
    except:
        continue
       
        


df= pd.DataFrame(listing)
df.to_csv('imdb13.csv', index =False)

