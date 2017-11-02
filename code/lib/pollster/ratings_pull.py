#! /usr/bin/python

# Pulls ratings from Pollster

import pandas as pd
import csv
import requests
from datetime import datetime, timedelta, date



CSV_URL = 'https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv'


class DataRead(object):
    def __init__(self):
        self.CSV_URL = CSV_URL

    def get_data(self, CSV_URL):
        with requests.Session() as s:
            download = s.get(CSV_URL)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)

        # Necessary variables, comments just for chunking
        """Pandas variables"""
        url = CSV_URL
        df = pd.read_csv(url)
        approval_is = "############# Approval is: {} #############"
        query_string ='subgroup == "All polls" & pollster == "Gallup" & approve > 0 & createddate == "{}"'
        """Time variables""" # TODO: Is there a better way to do this?

        today = date.today()
        today_date = today.strftime("%m/%d/%Y")

        yesterday = date.today() - timedelta(1)
        yesterday_date = yesterday.strftime("%m/%d/%Y")

        two_days = date.today() - timedelta(2)
        two_days_date = two_days.strftime("%m/%d/%Y")


        # End variables

        try:
            fresh_gallup = (df.query(query_string.format(today_date)))
            approval = int(fresh_gallup.approve)
            print(approval_is.format(approval))
            return approval
        except TypeError:
            fresh_gallup = (df.query(query_string.format(yesterday_date)))
            approval = int(fresh_gallup.approve)
            print(approval_is.format(approval))
            return approval
        else:
            fresh_gallup = (df.query(query_string.format(two_days_date)))
            approval = int(fresh_gallup.approve)
            print(approval_is.format(approval))
            return approval
