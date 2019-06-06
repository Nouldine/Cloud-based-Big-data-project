
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.markup import remove_tags
from sports.items import SportsItem



class SportSpider(CrawlSpider):

    name = "sports"

    allow_domains = ["www.espn.com"]

    start_urls = [ 

            "http://www.espn.com/"

            ]

    download_delay = 1

    rules = (

        Rule( LinkExtractor( allow=(r'http://www.espn.com/')),

            callback = 'parse_item',

            follow = True


            ),

        )



    def parse_item( self, response ):

        paragraphs = response.selector.xpath("//p").extract()

        item = SportsItem()

        item['feed'] = "".join( remove_tags(paragraph).encode('utf-8') for paragraph in paragraphs )

        yield item
