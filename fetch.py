import numpy as np
import pandas as pd
import csv
import glob
import re
text=[]
tokens = []
stopwords=[]

def changes():
    df = pd.read_csv('ir-news-2-4.csv', encoding="utf-8") 
    text = df.content
    #print(text)
    for line in text:
        
        ac1 = re.sub(r"\d", " ", line)
        ac2 = re.sub(r'<[^>]+>', " ", ac1)
        ac3 = re.sub(r'[^\w\s]', ' ', ac2)
        ac4 = ac3
        # print(ac4)
    
        tokens = ac4.split()
            
        #print(tokens)
        # with open("stopwords.txt") as fp: 
        #     for line_S in fp:
        #         print(line_S) 

        text_file = open("stopwords.txt", "r")
        lines = text_file.readlines()
        print (lines)
        
        text_file.close()
        



changes()
# print(text)