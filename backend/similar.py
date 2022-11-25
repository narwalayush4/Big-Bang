import pandas
import csv
import ast
df = pandas.read_csv('imdb_final.csv')
similar_movies=df["similar"].tolist()
listed_similar_movies=[]
for e in similar_movies:
    listed_similar_movies.append(ast.literal_eval(e))
# listed_similar_movies=ast.literal_eval(similar_movies)
# print(similar_movies[0])
movie_id=df["movie_id"].tolist()
 #print(movie_title[0])
# print(movie_id[0])
relevant_similar_movies_posters=[] #posters of similar movies
for i in range(len(movie_id)):
    relevant_similar_movies_posters.append([])

poster=df["poster"].tolist()
id_poster = {movie_id[i]: poster[i] for i in range(len(movie_id))}

for i in range(len(movie_id)):
    for s in listed_similar_movies[i]:
        s_stripped=s[7:-1]
        if s_stripped in movie_id:
            relevant_similar_movies_posters[i].append(id_poster.get(s_stripped))

df['relevant_similar_posters']=relevant_similar_movies_posters
title=df["movie_title"].tolist()
id_title = {movie_id[i]: title[i] for i in range(len(movie_id))}
relevant_similar_movies_titles=[]#titles of similar movies

for i in range(len(movie_id)):
    relevant_similar_movies_titles.append([])

for i in range(len(movie_id)):
    for s in listed_similar_movies[i]:
        s_stripped=s[7:-1]
        if s_stripped in movie_id:
            relevant_similar_movies_titles[i].append(id_title.get(s_stripped))


df['relevant_similar_titles']=relevant_similar_movies_titles

relevant_similar_movies_title1=[]


for i  in range(len(relevant_similar_movies_titles)):
    if(len(relevant_similar_movies_titles[i])==0):
        relevant_similar_movies_title1.append("null")
    else:
        relevant_similar_movies_title1.append(relevant_similar_movies_titles[i][0])

relevant_similar_movies_title2=[]

for i  in range(len(relevant_similar_movies_titles)):
    if len(relevant_similar_movies_titles[i])<=1 :
        relevant_similar_movies_title2.append("null")
    else:
        relevant_similar_movies_title2.append(relevant_similar_movies_titles[i][1])

relevant_similar_movies_title3=[]

for i  in range(len(relevant_similar_movies_titles)):
    if len(relevant_similar_movies_titles[i])<=2 :
        relevant_similar_movies_title3.append("null")
    else:
        relevant_similar_movies_title3.append(relevant_similar_movies_titles[i][2])

relevant_similar_movies_title4=[]

for i  in range(len(relevant_similar_movies_titles)):
    if len(relevant_similar_movies_titles[i])<=3 :
        relevant_similar_movies_title4.append("null")
    else:
        relevant_similar_movies_title4.append(relevant_similar_movies_titles[i][3])

title_poster = {title[i]: poster[i] for i in range(len(movie_id))}

relevant_similar_movies_poster1=[]


for i in range(len(relevant_similar_movies_title1)):
    if(relevant_similar_movies_title1[i]) == "null":
        relevant_similar_movies_poster1.append("null")
    else:
        relevant_similar_movies_poster1.append(title_poster.get(relevant_similar_movies_title1[i]))

relevant_similar_movies_poster2=[]


for i in range(len(relevant_similar_movies_title2)):
    if(relevant_similar_movies_title2[i]) == "null":
        relevant_similar_movies_poster2.append("null")
    else:
        relevant_similar_movies_poster2.append(title_poster.get(relevant_similar_movies_title2[i]))

relevant_similar_movies_poster3=[]


for i in range(len(relevant_similar_movies_title3)):
    if(relevant_similar_movies_title3[i]) == "null":
        relevant_similar_movies_poster3.append("null")
    else:
        relevant_similar_movies_poster3.append(title_poster.get(relevant_similar_movies_title3[i]))

relevant_similar_movies_poster4=[]


for i in range(len(relevant_similar_movies_title4)):
    if(relevant_similar_movies_title4[i]) == "null":
        relevant_similar_movies_poster4.append("null")
    else:
        relevant_similar_movies_poster4.append(title_poster.get(relevant_similar_movies_title4[i]))


df['relevant_similar_movies_title1']=relevant_similar_movies_title1
df['relevant_similar_movies_title2']=relevant_similar_movies_title2
df['relevant_similar_movies_title3']=relevant_similar_movies_title3
df['relevant_similar_movies_title4']=relevant_similar_movies_title4
df['relevant_similar_movies_poster1']=relevant_similar_movies_poster1
df['relevant_similar_movies_poster2']=relevant_similar_movies_poster2
df['relevant_similar_movies_poster3']=relevant_similar_movies_poster3
df['relevant_similar_movies_poster4']=relevant_similar_movies_poster4
df.drop_duplicates(subset="movie_title",
                     keep="first", inplace=True)
  
df.to_csv('imdb_final4.csv',index=False)








# df.to_csv('imdbfinal2.csv',index=False)



                



