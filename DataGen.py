import pandas as pd
from faker import Faker
import csv
def generate_data():
    output = open('Data/CSV/Datagen.CSV', 'w', newline='');
    fake=Faker()
    header = ['Customerid','Name','Age','Street','City','State','Zip']
    mywritter = csv.writer(output)
    mywritter.writerow(header)

    for i in range(100):
        mywritter.writerow([i+1,fake.name(),fake.random_int(18,80,1),fake.street_address(),fake.city(),
                            fake.state(),fake.zipcode()])
    output.close()

