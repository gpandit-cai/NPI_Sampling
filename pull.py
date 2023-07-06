
import requests
import pandas as pd
import numpy as np
import json
from pandas import json_normalize

import os

from app import fetch_npi_data

#os.chdir('C:\Users\GopinathPandit\OneDrive - ConcertAI\Python\Python_Practice')

raw_input = pd.read_csv('NPI.csv',names= ['NPI'])

for k in range(1,6):

    raw_data = pd.DataFrame()
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()

    empty = []

    for i in raw_input['NPI'].sample(n = 1000):
        if fetch_npi_data(i)['result_count'] > 0:
            #print('Yes')
            
            df1 = pd.json_normalize(fetch_npi_data(i)['results'])
            raw_data = pd.concat([raw_data,df1])

        else:
            empty.append(i)

    no_data = pd.DataFrame(empty, columns= ['NPI'])

    raw_data = raw_data[['number','basic.first_name',
    'basic.last_name',
    'basic.middle_name',
    'basic.credential',
    'basic.sole_proprietor',
    'basic.gender',
    'basic.enumeration_date',
    'basic.last_updated',
    'basic.certification_date',
    'basic.status']]

    writer = pd.ExcelWriter(f'NPI_Output_{k}.xlsx')
    raw_data.to_excel(writer, sheet_name='NPI_Details', index=False)
    no_data.to_excel(writer, sheet_name='Deactive-Invalid_NPI', index=False)
    writer.close()
                    
    
    
    

