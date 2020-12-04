import numpy as np
import pandas as pd
import csv
import glob
import re
text=[]
ac4 = []

def changes():
    df = pd.read_csv('ir-news-2-4.csv', encoding="utf-8") 
    text = df
    #print(text)
    for line in text:
        ac1 = re.sub(r"\d", " ", line)
        ac2 = re.sub(r'<[^>]+>', " ", ac1)
        ac3 = re.sub(r'[^\w\s]', ' ', ac2)
        ac4 = ac3




changes()
# print(text)