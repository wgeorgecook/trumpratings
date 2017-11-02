#! /usr/bin/python

# Pulls ratings from Pollster

import pandas as pd
import csv
import requests
from datetime import datetime, timedelta, date



CSV_URL = 'https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv'
approval_list = []

def get_data(CSV_URL):
    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

    # Necessary variables, comments just for chunking
    url = CSV_URL
    df = pd.read_csv(url)
    today = date.today()
    today_date = today.strftime("%m/%d/%Y")
    today = date.today()
    yesterday = date.today() - timedelta(1)
    yesterday_date = yesterday.strftime("%m/%d/%Y")
    created_date = today_date
    # End variables

    try:
        fresh_gallup = (df.query('subgroup == "All polls" & pollster == "Gallup" & approve > 0 & createddate == "{}"'.format(created_date)))
        approval = int(fresh_gallup.approve)
        print("Approval is:", approval)
        return approval
    except TypeError:
        fresh_gallup = (df.query('subgroup == "All polls" & pollster == "Gallup" & approve > 0 & createddate == "{}"'.format(yesterday_date)))
        approval = int(fresh_gallup.approve)
        print("Approval is:", approval)
        return approval
