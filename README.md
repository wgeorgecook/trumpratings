# Trump's Approval Rating

## Introduction
This bot was an idea I had during the turbulent up and downs of the early Trump presidency. While his approval and disapproval numbers were in flux, I wanted a way to put those numbers into context of his Twitter habits. I also wanted to archetect a Python application myself, and though I did get some help from Michael Pentecost, I think I largely acheived this goal. You may find this bot tweeting as [@TrumpsRatings](https://twitter.com/trumpsratings) on Twitter.

## Background
### Current Production
[Dustin Miller](https://www.twitter.com/spdustin) suggested that I improve Trumps Ratings by scraping [Gallup's](https://news.gallup.com/poll/203198/presidential-approval-ratings-donald-trump.aspx) website directly to get approval ratings. Finally and nearly a year later, it does just that! @TrumpsRatings uses the [lxml](https://lxml.de/index.html) library to parse the webpage directly. Finally, it gathers @realDonaldTrump's latest tweet, parses the tweet URL, and tweets back latest approval/disapproval numbers. The President's last tweet is embedded in @TrumpsRatings. At present deployment, the bot is started by a cron job on my server which runs every fifteen minutes.
### Previous Iterations
This Twitter bot originally streamed ratings data from [fivethirtyeight](https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv).
It parsed through the data to get the most recent Gallup approval rating. All of this utilized the amazing [Pandas](https://pandas.pydata.org/) library.

## Deployment
I highly suggest downloading [Vagrant](https://vagrantup.com), as the deployment scripts in `deployment` will work out the box. Once you've got Vagrant installed locally, clone this repository and `cd` into `/deployment`. From there, run `vagrant up` and the Vagrantfile will download a copy of Ubuntu server, download the required apt packages, and create a virtual Python environment. Pip packages in `/deployment/requirements.txt` will then install.
- You'll need to populate `settings.py` with your own Twitter API information, see below.

## Configure API details
Make a copy of `settings_template.py` and name it `settings.py`. Create a [Twitter developer](https://developer.twitter.com/content/developer-twitter/en.html) account and generate your own consumer key, consumer secret, access token, and access secret. Copy and paste those values into their respective dictionary key values.

## Database
Relevant tweet info is passed to a PostgreSQL database and checked for previous usage before attempting to post a new tweet that might be duplicate. This database is created via the `deployment/pg_hba.conf` and `psql_setup.sql` files. Make modifications to them if you want your table or columns to have different names, but also update the corresponding values in `settings.py`.

## TrumpRatings Future
I know there are many different polling data visualization websites on the internet, but I'd like to make my own. I have data from November 2017 that corresponds to tweets and national events. Perhaps Angular or React would be a good way to display this data. I also notice that a lot of (probably) other bots will retweet and respond to @trumpratings. I wonder what might happen if I gave @trumpratings the ability to respond to engagement.

## Contributing
I'd love if you want to help make @TrumpRatings better! If you see an issue or would like to make a new feature, please clone the repo and implement your fix/feature. Submit a pull request with a detailed comment of the bug you fixed or a feature you implemented. Please do local tests and make sure it doesn't break existing features in `master`.