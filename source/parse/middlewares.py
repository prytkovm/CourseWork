# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random
from scrapy import signals
import os
import requests
import json
import logging
from urllib.parse import urljoin, urlparse

from w3lib.url import safe_url_string

from scrapy.http import HtmlResponse
from scrapy.utils.response import get_meta_refresh
from scrapy.exceptions import IgnoreRequest, NotConfigured

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from stem import Signal
from stem.control import Controller


# class ProxyMiddleware(object):
#
#     def process_request(self, request, spider):
#         # Set the location of the proxy
#         request.meta['proxy'] = self.get_proxies()
#         print("Got!")
#         # # Use the following lines if your proxy requires authentication
#         # request.headers['Proxy-Authorization'] = 'Basic'
#
#     def get_proxies(self):
#         result = []
#         json_data = {"method": "get", "model": "proxy", "limit": 1, "fields": "address,response_time"}
#         url = "http://127.0.0.1:55555/api/v1/"
#
#         response = requests.post(url, json=json_data)
#         if response.status_code == 200:
#             response = json.loads(response.text)
#             for proxy in response["data"]:
#                 result.append(proxy["address"])
#         # protocol = result[0].split(":")[0]
#         print(result)
#         return result[0]
#         # return {
#         #     'http': str(result[0]),
#         #     'https': str(result[0])
#         # }
#

class UserAgentMiddleware:
    """This middleware allows spiders to override the user_agent"""

    def __init__(self, user_agent=''):
        self.user_agent = user_agent
        self.path = os.getcwd()

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings['USER_AGENT'])
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        self.user_agent = getattr(spider, 'user_agent', self.user_agent)

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers.setdefault(b'User-Agent', self.user_agent)


class RollingUserAgentMiddleware(UserAgentMiddleware):

    def __init(self, user_agent=''):
        self.user_agent = user_agent
        super(RollingUserAgentMiddleware, self).__init__()

    def process_request(self, request, spider):
        with open(self.path + "\\parse\\user_agents.txt") as agents:
            ua = random.choice(agents.read().splitlines())
            if ua:
                request.headers.setdefault('User-Agent', ua)
                spider.log(
                    'User-Agent: {} {}'.format(request.headers.get('User-Agent'), request)
                )


class ParseSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# class RedirectMiddleware(ParseSpiderMiddleware):
#     """
#     Handle redirection of requests based on response status
#     and meta-refresh html tag.
#     """
#
#     def process_response(self, request, response, spider):
#         if (
#             request.meta.get('dont_redirect', False)
#             or response.status in getattr(spider, 'handle_httpstatus_list', [])
#             or response.status in request.meta.get('handle_httpstatus_list', [])
#             or request.meta.get('handle_httpstatus_all', False)
#         ):
#             return response
#
#         allowed_status = (301, 302, 303, 307, 308)
#         if 'Location' not in response.headers or response.status not in allowed_status:
#             return response
#
#         location = safe_url_string(response.headers['Location'])
#         if response.headers['Location'].startswith(b'//'):
#             request_scheme = urlparse(request.url).scheme
#             location = request_scheme + '://' + location.lstrip('/')
#
#         redirected_url = urljoin(request.url, location)
#
#         if response.status in (301, 307, 308) or request.method == 'HEAD':
#             redirected = request.replace(url=redirected_url)
#             return self._redirect(redirected, request, spider, response.status)
#
#         redirected = self._redirect_request_using_get(request, redirected_url)
#         return self._redirect(redirected, request, spider, response.status)


class ParseDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)