import numpy as np
import pandas as pd
import csv
import glob
import re
text=[]


def changes():
    df = pd.read_csv('ir-news-2-4.csv', encoding="utf-8") 
    text = df.content
    print(text)
    for line in text:
        
        ac1 = re.sub(r"\d", " ", line)
        ac2 = re.sub(r'<[^>]+>', " ", ac1)
        ac3 = re.sub(r'[^\w\s]', ' ', ac2)
        ac4 = ac3
        for l in ac4:
            ac4 = re.sub(l, ' ', ac4)
            tokens = ac4.split()
            #print(tokens)
        # print(ac4)
        # channel_values = open(ac4).read().split()
        # print(channel_values)

        



changes()
# print(text)