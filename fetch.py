
import pandas as pd
import re
from nltk.tokenize import word_tokenize

# text = "Nick likes to play football, however he is not too fond of tennis."
# text_tokens = word_tokenize(text)
# print(text_tokens)

text = list()
df = pd.read_csv('ir-news-2-4.csv')
text = df.content
for line in text:
    ac1 = re.sub(r"\d", " ", line)
    ac2 = re.sub(r'<[^>]+>', " ", ac1)
    ac3 = re.sub(r'[^\w\s]', ' ', ac2)
    ac4 = ac3
    tokens = []

    #tokens = ac4.split(" ")
    text_tokens = word_tokenize(ac4)
   # print(text_tokens)
   # print(tokens)


text_s = list()
read_file = pd.read_csv('stop_words.txt')
#read_file.columns = ['first']
read_file.to_csv(r'stopwords_convert.csv', index=None)

df1 = pd.read_csv('stopwords_convert.csv')


#print(df1)

#text_s = df1.first
#print(text_s)

#tokens_without_sw = [word for word in text_tokens if not word in ]

#print(tokens_without_sw)
