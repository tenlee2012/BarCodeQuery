#!/bin/env python3
# coding = utf-8


import requests
import logging
import random
import re

from .code import good_detail_code
from .good import Good

logging.basicConfig(level=logging.INFO)


class BarCodeSpider:
    logger = logging.getLogger(__name__)
    '''
    条形码爬虫类
    '''
    user_agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko)'
        'Chrome/17.0.963.12 Safari/535.11',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)']

    base_url = 'http://search.anccnet.com/searchResult2.aspx'

    @classmethod
    def get_html_by_barcode(cls, barcode):
        payload = {'keyword': barcode}
        headers = {'user-agent': cls.user_agent[random.randint(0, 3)]}
        search_page = requests.get(
            cls.base_url, params=payload, headers=headers)

        pattern = re.compile(
            r'([\s\S]*?)<dd><a href="(.*)" target="_blank">' +
            barcode +
            '</a></dd>([\s\S]*?)')
        m = pattern.match(search_page.text)
        if None == m:
            return None

        good_detail_url = m.group(2)
        cls.logger.info(
            "barcode {} url is {}".format(
                barcode, good_detail_url))

        good_detail_page = requests.get(good_detail_url, headers=headers)

        if (good_detail_page.status_code == 200):
            return good_detail_page.text
        else:
            cls.logger.error(
                "error, status code is {}, content is {}".format(
                    good_detail_page.status_code,
                    good_detail_page.text))
            return None

    @classmethod
    def get_good(cls, barcode):
        good = Good()
        good.barcode = barcode

        html = cls.get_html_by_barcode(barcode)
        if html is None:
            return good
        for key in good_detail_code:
            values = good_detail_code[key]

            # 字符串
            if isinstance(values, str):
                pattern = re.compile(
                    r"([\s\S]*?)SetValue\('" + values + "','(.*)'\)([\s\S]*?)")
                m = pattern.match(html)
                if m is not None:
                    result = m.group(2)
                    result = result.replace('&nbsp;', ' ')
                    setattr(good, key, result)
                else:
                    setattr(good, key, "")
            else:  # 元组
                result = ""
                for value in values:
                    pattern = re.compile(
                        r"([\s\S]*?)SetValue\('" + value + "','(.*)'\)([\s\S]*?)")
                    m = pattern.match(html)
                    if m is not None:
                        result += m.group(2)
                setattr(good, key, result)

        cls.logger.info("result is {}".format(good.__dict__))
        return good


def main():
    good = BarCodeSpider.get_good('06917878036526')
    print(good.__dict__)


if __name__ == '__main__':
    main()
