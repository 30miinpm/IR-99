import pandas as pd
import csv
import glob




df = pd.read_csv('ir-news-2-4.csv', encoding="utf-8")

dfw = pd.DataFrame(df)
text=[]


text = dfw.content

print(text)