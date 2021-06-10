import scrapy
import urllib.parse
import json
from checktrade_scraper.items import ChecktradeScraperItem
from w3lib.url import add_or_replace_parameter


class ChecktrdeSpider(scrapy.Spider):
    name = 'checktrade'
    allowed_domains = ['wapi.checktrade.com']
    start_urls = ['https://checktrade.com/']

    postal_codes = ['SA1 3QW', 'CF10 2NX', 'BS1 3XB', 'BA1 1RT', 'TA6 5AW', 'EX4 3NJ', 'PL1 1RP', 'EX31 1HX', 'BH1 1DY',
                    'SO14 7LE', 'PO1 1AB', 'RG1 2AD', 'EC3M 1AJ', 'HP1 1BD', 'LU5 4ET', 'MK9 3QA', 'NN1 1AF', 'CB2 3BZ',
                    'PE1 1DP', 'LE1 4FR', 'OX1 1ZZ', 'OX16 5UE', 'CV1 1QX', 'B98 8AB', 'GL1 1AD', 'HR1 2AB', 'WR4 9WW',
                    'DY10 1DD', 'DY1 1PY', 'B2 4AA', 'WS1 1NW', 'TF3 4AF', 'ST16 2HN', 'SY1 1BN', 'LL11 1BE', 'CH1 1HH',
                    'CW1 2PU', 'ST4 1AA', 'DE1 1SD', 'NG1 3QD', 'NG31 6NE', 'NG24 1DH', 'LN5 7NU', 'NG18 1SN',
                    'S80 1EY', 'S40 1PA', 'S1 2AX', 'DN4 5NE', 'DN15 6EN', 'HU9 1AA', 'S70 1AA', 'LS2 7DZ', 'WF1 1AA',
                    'HD1 2BQ', 'BD1 1US', 'M2 1BB', 'SK1 1QF', 'WA5 1WA', 'WA7 1AA', 'L1 8BN', 'WN1 1AA', 'BL1 1RF',
                    'OL16 1LR', 'PR1 8BQ', 'BB1 6AT', 'LA1 1HZ', 'LA9 4AA', 'HG1 1TU', 'YO1 9QL', 'BD23 1RD', 'YO7 1LB',
                    'YO11 1LD', 'DL1 1LS', 'TS24 7RR', 'DH1 3NJ', 'SR1 1RR', 'NE1 7DE', 'CA3 8JY', 'EH1 1BQ', 'G1 2RD']
    categories_fn = 'categories.json'

    params = {
        'categoryId': '',
        'location': postal_codes[1],  # remove to scrape all postcodes
        'page': 1,
        'itemsPerPage': 100

    }

    def start_requests(self):
        # https://wapi.checkatrade.com/search/categories
        with open(self.categories_fn) as f:
            categories_data = json.load(f)
        categories = [(category['id'], category['label']) for category in categories_data]

        for cat_id, cat_label in categories:
            self.params['categoryId'] = cat_id
            url = f'https://wapi.checkatrade.com/search?{urllib.parse.urlencode(self.params)}'
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs={'cat_label': cat_label,
                                                                          'postal_code': self.params['location']})
            # remove to get all categories
            if int(cat_id) > 1000:
                break

    def parse(self, response, cat_label, postal_code):
        response_json = response.json()
        pages = response_json.get('pages')
        for page_num in reversed(range(1, pages+1)):    # to keep the page order
            next_page = add_or_replace_parameter(response.url, 'page', page_num)
            yield scrapy.Request(
                url=next_page,
                callback=self.scrape,
                cb_kwargs={'cat_label': cat_label,
                           'postal_code': postal_code},
                dont_filter=True    # to allow duplicate request
            )

    def scrape(self, response, cat_label, postal_code):
        response_json = response.json()
        output_item = ChecktradeScraperItem()
        items = response_json.get('items')
        if items:
            for item in items:
                output_item['company_name'] = item['name']
                output_item['unique_name'] = item['unique_name']
                output_item['email'] = item['email']
                output_item['mobile_phone'] = self.get_mobile(item)
                output_item['landline_phone'] = self.get_landline(item)
                output_item['cat_label'] = cat_label
                output_item['postal_code'] = postal_code
                yield output_item

    @staticmethod
    def get_mobile(item):
        phone_numbers = item.get('phone_numbers')
        if phone_numbers:
            for number in phone_numbers:
                if number.get('label'):
                    number = number.get('label')
                    if number[1] == '7':
                        return number
                    else:
                        continue
        return 'N/A'

    @staticmethod
    def get_landline(item):
        phone_numbers = item.get('phone_numbers')
        if phone_numbers:
            for number in phone_numbers:
                if number.get('label'):
                    number = number.get('label')
                    if number[1] == '1':
                        return number
                    else:
                        continue
        return 'N/A'
