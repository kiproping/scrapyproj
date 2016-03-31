# -*- coding: utf-8 -*-
import scrapy

from jackpot.items import JackpotItem

class SportpesaSpider(scrapy.Spider):
	name = "sportpesa"
	allowed_domains = ["sportpesa.com"]
	start_urls = (
		'https://www.sportpesa.com/games/jackpot_games/',
	)

	def parse(self, response):

		tablerows = response.css('table.mod-table tbody tr')

		for tr in tablerows:
			td = tr.xpath('td')
			item = JackpotItem()

			item['pos'] =  td[0].xpath('text()').extract()
			item['time'] = td[1].xpath('text()').extract()
			item['date'] = td[2].css('span.text-left').xpath('text()').extract()
			item['flag'] = td[2].css('span.text-right').xpath('img/@src').extract()
			item['homet'] = td[3].css('span.text-left').xpath('text()').extract()
			item['hometodds'] = td[3].css('span.text-right span.text-right').xpath('text()').extract()
			item['drawodds'] = td[4].xpath('text()').extract()
			item['awayt'] = td[5].css('span.text-left').xpath('text()').extract()
			item['awaytodds'] = td[5].css('span.text-right').xpath('text()').extract()
			item['result'] = td[6].xpath('text()').extract()
			yield(item)
