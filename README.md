# Trump's Approval Rating

Find this bot tweeting as @TrumpsRatings on Twitter.

This Twitter bot streams ratings data from [fivethirtyeight](https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv).
It parses through the data to get the most recent Gallup approval rating. Finally, it gathers @realDonaldTrump's latest tweet, parses the tweet URL, and tweets back latest approval/disapproval numbers. The President's last tweet is embedded in @TrumpsRatings.

Relevant tweet info is passed to a database and checked for previous usage before attempting to post a new tweet that might be duplicate.

Referenced settings are stored as dictionaries in settings.py (see settings_template.py).
