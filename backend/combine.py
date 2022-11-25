# import pandas as pd
# import glob
# import os
  
# # merging the files
# joined_files = os.path.join("/Home", "imdb*.csv")
  
# # A list of all joined files is returned
# joined_list = glob.glob(joined_files)
  
# # Finally, the files are joined
# df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
# print(df)

import pandas as pd
  
# merging two csv files

df = pd.concat(
    map(pd.read_csv, ['imdb1.csv', 'imdb2.csv','imdb3.csv','imdb4.csv','imdb5.csv', 'imdb6.csv', 'imdb7.csv', 'imdb8.csv', 'imdb9.csv', 'imdb10.csv', 'imdb11.csv', 'imdb12.csv', 'imdb13.csv' ]), ignore_index=True)
length = len(df)
lang="Hindi"
language=[]
for i in range(839):
    language.append(lang)
df['Language']=language
# df.to_csv('imdb.csv', index=False)