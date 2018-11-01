from lxml import html
import requests


class GetRatings(object) :
    """
    Scrapes Gallup webpage to gather most recent
    approval and disapproval poll data.
    """
    def __init__(self):
        self.page = requests.get('https://news.gallup.com/poll/203198/presidential-approval-ratings-donald-trump.aspx')
        self.tree = html.fromstring(self.page.content)

    def scrape_page(self):

        # The tree spits out an array. We need the first index.
        raw_disapprove = self.tree.xpath('//*[@id="20170130140453"]/div/table/tbody[1]/tr[2]/td[2]/text()')
        raw_approve = self.tree.xpath('//*[@id="20170130140453"]/div/table/tbody[1]/tr[2]/td[1]/text()')
        approve = raw_approve[0]
        disapprove = raw_disapprove[0]

        # Twitter method will expect an array with approve and disapprove
        return [approve, disapprove]
