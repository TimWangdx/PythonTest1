from UrlManager import *
from HtmlDownloader import *

class SpiderManager(object):
    def __init__(self):
        self.urlManager = UrlManager()
        self.htmlDownloader = HtmlDownloader()

    def craw(self, root_url):
        html = self.htmlDownloader.download(root_url)
        print(html)
