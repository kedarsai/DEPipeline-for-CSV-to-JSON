import DataGen
import time
from datetime import datetime
import shutil
import os
import utility
import SQL

if __name__ == '__main__':
    for i in range(2):
        DataGen.generate_data()
        print("Data generated on {}".format(datetime.now()))
        time.sleep(1)
        utility.csv2Json('Data/CSV/Datagen.CSV')
    utility.movejson()

    SQL.insertfromcsv('Data/CSV/Datagen.CSV')




