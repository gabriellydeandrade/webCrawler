# -*- encoding: utf-8 -*-
# Created on 2018-01-13 16:44:21
# Project: epocacosmeticos
# Author: Gabrielly de Andrade

import unittest
from bs4 import BeautifulSoup
from crawler import Crawler

'''
class Counter(object):
    def __init__(cls):
        cls.count = 0

    def increment(cls):
        cls.count += 1
'''

class TestCrawler(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.instance_driver = Crawler()

    def test_get_categories(cls):
        result = cls.instance_driver.get_categories("http://www.epocacosmeticos.com.br/")
        cls.assertEqual(result, ['https://www.epocacosmeticos.com.br/perfumes',
                                  'https://www.epocacosmeticos.com.br/cabelos',
                                  'https://www.epocacosmeticos.com.br/maquiagem',
                                  'https://www.epocacosmeticos.com.br/dermocosmeticos',
                                  'https://www.epocacosmeticos.com.br/tratamentos',
                                  'https://www.epocacosmeticos.com.br/corpo-e-banho',
                                  'https://www.epocacosmeticos.com.br/unhas',
                                  'https://www.epocacosmeticos.com.br/lancamentos',
                                  'https://www.epocacosmeticos.com.br/ganhe-brindes',
                                  'https://www.epocacosmeticos.com.br/quero-cupom'])

    def test_get_title(cls):
        file_name = open("../tests_files/product_cabelo.html", "r", encoding="utf8")
        soup = BeautifulSoup(file_name.read(), "lxml")
        result = cls.instance_driver.get_title("product_cabelo.html", soup)
        cls.assertEqual(result, "Mascara de Reconstrucao Lola Cosmetics Argan Oil - Epoca Cosmeticos")
        file_name.close()
    '''
    def test_visit_categories(cls):
        cls.instance_driver.visit_categories(["perfumes", "cabelos"])
        cls.instance_driver.extract_products()

    def test_extract_products_calls(cls):
        c = Counter()
        c.increment()
        cls.assertEqual(1, c.count)
    '''


if __name__ == '__main__':
    unittest.main()






















'''
class webCrawlerTest(unittest.TestCase):

	def csvFile(cls):
		csvFile = open("../results.csv","w", newline='')
		file = csv.writer(csvFile)
		file.writerow(["title","productName","url"])
		csvFile.close()

	def appendCsvFile(cls, title, productName, url):
		with open("../results.csv","a", newline='') as csvFile:
			write = csv.writer(csvFile)
			write.writerow([title , productName , url])
		csvFile.close()

	def setUp(cls):
		cls.driver = webdriver.Chrome()

	def extractFromURL(cls, url):
		for numberPage in range (1,2):
			driver = cls.driver
			driver.get("http://www.epocacosmeticos.com.br/selecao/acao#1")
			#driver.get(url + str(numberPage))

			titleList = driver.find_elements_by_xpath("//span[@class='shelf-default__brand']/a")
			productNameList = driver.find_elements_by_class_name("shelf-default__item")
			urlList = driver.find_elements_by_class_name("shelf-default__link")

			for i in range (len(titleList)):
				cls.appendCsvFile(titleList[i].text, productNameList[i].get_attribute("title"), \
				urlList[i].get_attribute("href"))	
	
	def tearDown(cls):
		cls.driver.close()


def main ():
	webCrawler().csvFile()
	webCrawler().extractFromURL("http://www.epocacosmeticos.com.br/selecao/acao#")

if __name__ == '__main__':
    unittest.main()

  '''