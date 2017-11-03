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
        url = self.CSV_URL
        df = pd.read_csv(url)
        approval_is = "############# Approval is: {} #############"
        approval_string ='subgroup == "All polls" & pollster == "Gallup" & approve > 0 & createddate == "{}"'
        disapproval_string ='subgroup == "All polls" & pollster == "Gallup" & disapprove > 0 & createddate == "{}"'
        disapproval_is = "Disapproval is: {} #############"
        """Time variables""" # TODO: Is there a better way to do this?

        today = date.today()
        today_date = today.strftime("%m/%d/%Y")

        yesterday = date.today() - timedelta(1)
        yesterday_date = yesterday.strftime("%m/%d/%Y")

        two_days = date.today() - timedelta(2)
        two_days_date = two_days.strftime("%m/%d/%Y")

        three_days = date.today() - timedelta(3)
        three_days_date = three_days.strftime("%m/%d/%Y")


        # End variables

        try:
            approve_gallup = (df.query(approval_string.format(today_date)))
            disapprove_gallup = (df.query(disapproval_string.format(today_date)))
            approval = int(approve_gallup.approve)
            disapproval = int(disapprove_gallup.disapprove)
            print(approval_is.format(approval), disapproval_is.format(disapproval))
            return approval, disapproval
        except TypeError:
            try:
                approve_gallup = (df.query(approval_string.format(yesterday_date)))
                disapprove_gallup = (df.query(disapproval_string.format(yesterday_date)))
                approval = int(approve_gallup.approve)
                disapproval = int(disapprove_gallup.disapprove)
                print(approval_is.format(approval), disapproval_is.format(disapproval))

                return approval, disapproval
            except TypeError:
                try:
                    approve_gallup = (df.query(approval_string.format(two_days_date)))
                    disapprove_gallup = (df.query(disapproval_string.format(two_days_date)))
                    approval = int(approve_gallup.approve)
                    disapproval = int(disapprove_gallup.disapprove)
                    print(approval_is.format(approval), disapproval_is.format(disapproval))
                    return approval, disapproval
                except TypeError:
                    approve_gallup = (df.query(approval_string.format(three_days_date)))
                    disapprove_gallup = (df.query(disapproval_string.format(three_days_date)))
                    approval = int(approve_gallup.approve)
                    disapproval = int(disapprove_gallup.disapprove)
                    print(approval_is.format(approval), disapproval_is.format(disapproval))
                    return approval, disapproval
