import os
import shutil
import pandas as pd
import json
import csv
from datetime import datetime

def movejson():
    path = r'C:\Users\Kedar Sai\PycharmProjects\DEpython'
    for x in os.listdir(path):
        if x.endswith(".json"):
            print(x)
            shutil.move(x,'Data/Json')
            print("{} moved to JSON Folder".format(x))



def csv2Json(file):
    df=pd.read_csv(file)
    now = datetime.now().strftime("%H%M%S")
    opfile = 'Datagen '+str(now)+'.json'
    df.to_json(opfile)
    print("Successfully converted into Json")