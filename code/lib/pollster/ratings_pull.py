
# Pulls ratings from Pollster

import pandas as pd
import csv
import requests
from datetime import datetime, timedelta, date



CSV_URL = 'https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv'

class DataRead(object):

    """
    Streams the CSV with relevant polling data.
    Searches for most recent polling data from Gallup
    by starting for an end date of today and going
    backwards a day at a time until valid data returned
    """

    def __init__(self):
        self.CSV_URL = CSV_URL

    def get_data(self, CSV_URL):


        # Necessary variables, comments just for chunking
        # Pandas variables
        url = self.CSV_URL
        df = pd.read_csv(url)
        approval_is = "############# Approval is: {} #############"
        approval_string ='subgroup == "All polls" & pollster == "Gallup" & enddate == "{}"'
        disapproval_string ='subgroup == "All polls" & pollster == "Gallup" & enddate == "{}"'
        disapproval_is = "Disapproval is: {} #############"

        # Timestamp variables
        today = date.today()
        today_date = today.strftime("%m/%-d/%Y")

        yesterday = date.today() - timedelta(1)
        yesterday_date = yesterday.strftime("%m/%-d/%Y")

        two_days = date.today() - timedelta(2)
        two_days_date = two_days.strftime("%m/%-d/%Y")

        three_days = date.today() - timedelta(3)
        three_days_date = three_days.strftime("%m/%-d/%Y")

        four_days = date.today() - timedelta(4)
        four_days_date = four_days.strftime("%m/%-d/%Y")

        five_days = date.today() - timedelta(5)
        five_days_date = five_days.strftime("%m/%-d/%Y")

        six_days = date.today() - timedelta(6)
        six_days_date = six_days.strftime("%m/%-d/%Y")

        seven_days = date.today() - timedelta(7)
        seven_days_date = seven_days.strftime("%m/%-d/%Y")

        eight_days = date.today() - timedelta(8)
        eight_days_date = eight_days.strftime("%m/%-d/%Y")
        # End timestamp variables

        # Try/except blocks will go back in time a day at a time
        # iterating over the CSV with polling data until
        # valid data is returned.
        # TODO: Is there a better way to do this?

        try:
            approve_gallup = (df.query(approval_string.format(today_date)))
            disapprove_gallup = (df.query(disapproval_string.format(today_date)))
            approval = int(approve_gallup.approve)
            disapproval = int(disapprove_gallup.disapprove)
            print(approval_is.format(approval), disapproval_is.format(disapproval))
            return [approval, disapproval]

        except TypeError:
            try:
                approve_gallup = (df.query(approval_string.format(yesterday_date)))
                disapprove_gallup = (df.query(disapproval_string.format(yesterday_date)))
                approval = int(approve_gallup.approve)
                disapproval = int(disapprove_gallup.disapprove)
                print(approval_is.format(approval), disapproval_is.format(disapproval))
                return [approval, disapproval]

            except TypeError:
                try:
                    approve_gallup = (df.query(approval_string.format(two_days_date)))
                    disapprove_gallup = (df.query(disapproval_string.format(two_days_date)))
                    approval = int(approve_gallup.approve)
                    disapproval = int(disapprove_gallup.disapprove)
                    print(approval_is.format(approval), disapproval_is.format(disapproval))
                    return [approval, disapproval]

                except TypeError:
                    try:
                        approve_gallup = (df.query(approval_string.format(three_days_date)))
                        disapprove_gallup = (df.query(disapproval_string.format(three_days_date)))
                        approval = int(approve_gallup.approve)
                        disapproval = int(disapprove_gallup.disapprove)
                        print(approval_is.format(approval), disapproval_is.format(disapproval))
                        return [approval, disapproval]

                    except TypeError:
                        try:
                            approve_gallup = (df.query(approval_string.format(four_days_date)))
                            disapprove_gallup = (df.query(disapproval_string.format(four_days_date)))
                            approval = int(approve_gallup.approve)
                            disapproval = int(disapprove_gallup.disapprove)
                            print(approval_is.format(approval), disapproval_is.format(disapproval))
                            return [approval, disapproval]

                        except TypeError:
                            try:
                                approve_gallup = (df.query(approval_string.format(five_days_date)))
                                disapprove_gallup = (df.query(disapproval_string.format(five_days_date)))
                                approval = int(approve_gallup.approve)
                                disapproval = int(disapprove_gallup.disapprove)
                                print(approval_is.format(approval), disapproval_is.format(disapproval))
                                return [approval, disapproval]    
                            
                            except TypeError:
                                try:
                                    approve_gallup = (df.query(approval_string.format(six_days_date)))
                                    disapprove_gallup = (df.query(disapproval_string.format(six_days_date)))
                                    approval = int(approve_gallup.approve)
                                    disapproval = int(disapprove_gallup.disapprove)
                                    print(approval_is.format(approval), disapproval_is.format(disapproval))
                                    return [approval, disapproval]

                                except TypeError:
                                    try:
                                        approve_gallup = (df.query(approval_string.format(seven_days_date)))
                                        disapprove_gallup = (df.query(disapproval_string.format(seven_days_date)))
                                        approval = int(approve_gallup.approve)
                                        disapproval = int(disapprove_gallup.disapprove)
                                        print(approval_is.format(approval), disapproval_is.format(disapproval))
                                        return [approval, disapproval]

                                    except TypeError:
                                        try:
                                            approve_gallup = (df.query(approval_string.format(eight_days_date)))
                                            disapprove_gallup = (df.query(disapproval_string.format(eight_days_date)))
                                            approval = int(approve_gallup.approve)
                                            disapproval = int(disapprove_gallup.disapprove)
                                            print(approval_is.format(approval), disapproval_is.format(disapproval))
                                            return [approval, disapproval]

                                        finally:
                                            print("Cannot gather data at this time. Exiting.")
                                            exit 2