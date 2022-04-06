import csv
import pandas as pd
import json

with open('Data/CSV/Datagen.CSV', 'r') as f: #Instead of using the open comand directly use with open, this will help us in avoiding closing the reader manually also there are other benifits
    myreader = csv.DictReader(f) #DictReader will help us in reading each cell of data with name. Instead of calling row[1] we can say row['Name']. This allow better readability.
    headers = next(myreader)
    # for row in myreader:
    #     print(row['Name'])

#Using pandas

# df = pd.read_csv('Data/Datagen.CSV')
# print(df.head())

df= pd.read_json('csv2json.json')
print(df.head())


