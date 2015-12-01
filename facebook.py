# -*- coding: utf-8 -*-
'''Spider for truecaller.com,works only for limited number of searches'''
import scrapy
import re
import os
# provide your own authentication cookies
my_cookies = {"c_user": '************',"xs": '****************'}


class FacebookSpider(scrapy.Spider):

    '''This class contains the spider used for crawling facebook.com
    For more information,read documentation of scrapy at
    http://doc.scrapy.org/en/latest/
    '''
    name = "facebook"
    #allowed_domains = ["facebook.com"]
    start_urls = (
        'http://www.facebook.com/',
    )

    def parse(self, response):
        '''This function authenticates the user
         session using supplied cookies'''
        request =  scrapy.Request('http://www.facebook.com/',cookies=my_cookies, callback=self.parsestart)
        print args
        return request

    def parsestart(self, response,):
        '''This function crawls all the numbers
         provided as input.You canRun a for loop for
          more than 1 number,
          but total number of searches is limited'''
        number = open('number.txt','r')
        for no in number.readlines():
            url = response.url + 'search/str/' + str(no)[0:10] +'/keywords_users'
            request = scrapy.Request(url, callback=self.parsename,cookies=my_cookies)
            request.meta['number'] = str(no)[0:10]
            yield request
        number.close()

    def parsename(self, response):
        '''Provides the name of the numbers requested
         in parsestart and enters it in number.txt file'''
        f = open('number.txt' ,'a+')
        find = re.search(r'<div class="_5d-5">(.*?)</div>',response.body)
        f.write('\n'+ response.meta['number'] + '-' + find.group(1) + '\n')
        f.close()
