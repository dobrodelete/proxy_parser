import os
import re
import datetime
import json
import requests
import fake_useragent
from random import choice
from time import sleep
from bs4 import BeautifulSoup

#import parser  (\d{1,3}\.){3}\d{1,3}:(\d+)

def writer(proxy):
	try:
		print(proxy)
		with open('new_proxy.txt', 'a+') as file:
			file.write(proxy)
	except Exception as ex:
		print(ex)

def ua_header():
	ua = fake_useragent.UserAgent().random
	header = {
		'user-agent': ua
	}
	return header


def p_proxy():
	with open('parsing_proxy.txt') as file:
		data = file.read()
		all_proxy = data.split('\n')
		proxy = choice(all_proxy)

	proxies = {
		'http': f'socks5://{proxy}',
		'https': f'socks5://{proxy}'
	}
	return p_proxy

def get_html(link):
	print('get_html')

	proxies = {
		'http': 'socks5://5fYctA62:23xnKAnM@1193.201.127.113:53041',
		'https': 'socks5://5fYctA62:23xnKAnM@193.201.127.113:53041'
	}

	headers = {
		"accept-encoding": "gzip, deflate, br",
		"accept": "*/*",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
	}
	r = requests.get(link)
	if r.ok:
		return r.text

	print(r.status_code)

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	return soup

def rootjazz():
	print('get start parse ROOTJAZZ')
	try:
		url = 'https://rootjazz.com/proxies/proxies.txt'
		writer((get_html(url)))
	except:
		print('error rootjazz')
	print('finish parse ROOTJAZZ')

def proxypedia():
	print('get start parse PROXYPEDIA')
	try:
		url = 'https://proxypedia.org/'
		proxy = get_data(get_html(url))
		ul = proxy.find('ul')
		proxy = ul.find_all('a')
		for ip in proxy:
			writer(f'{ip.text}\n')
	except:
		print('proxypedia error')
	print('finish parse PROXYPEDIA')

def hinky():
	print('get start parse HINKY')
	for i in range(1, 12):
		try:
			if i == 1:
				table = get_data(get_html(f'http://www.mrhinkydink.com/proxies.htm'))
			else:
				table = get_data(get_html(f'http://www.mrhinkydink.com/proxies{i}.htm'))
			tr = table.find_all('tr', {'bgcolor': '#88ff88'})
			for item in tr:
				td = item.find_all('td')
				ip = td[0].text
				port = td[1].text
				writer(f'{ip}:{port}\n')

			if i == 1:
				table = get_data(get_html(f'http://www.mrhinkydink.com/proxies.htm'))
			else:
				table = get_data(get_html(f'http://www.mrhinkydink.com/proxies{i}.htm'))
			tr = table.find_all('tr', {'bgcolor': '#ffff88'})
			for item in tr:
				td = item.find_all('td')
				ip = td[0].text
				port = td[1].text
				writer(f'{ip}:{port}\n')
			
			sleep(3)
		except:
			print('hinky error')
	print('finish parse HINKY ')

def htmlweb():
	print('get start parse HTMLWEB')
	url = 'https://htmlweb.ru/analiz/proxy_list.php?p=1&perpage=20'
	try:
		page = get_data(get_html(url))
		count_page = int(page.find('div', class_='link_bar').find_all('a')[-1].text)
		sleep(20)
		y = 0
		for i in range(1, count_page + 1):
			try:
				soup = get_data(get_html(f'https://htmlweb.ru/analiz/proxy_list.php?p={i}&perpage=20'))
				table = soup.find('table', class_='tbl')
				all_proxy = table.find_all('td')
				x = 6
				for line_proxy in all_proxy:
					if x % 6 == 0:
						print(line_proxy.text)
						writer(f'{line_proxy.text}\n')
					else:
						pass
						y += 1
				if y == 5:
					break
				else:
					continue
					x += 1

				sleep(15)
			except:
				print('cycle error')
	except:
		print('htmlweb error')

	print('finish parse HTMLWEB')

def hidemyname():
	print('get start parse HIDEMYNAME')
	try:
		url = 'https://hidemy.name/ru/proxy-list/#list'
		l = 'https://hidemy.name/ru/proxy-list/?start=3392#list'
		page = get_data(get_html(url))
		temp_page = page.find('div', class_='pagination').find('ul')
		count_page = int(temp_page.find_all('li')[8].text)
		sleep(10)
		a = 1
		for i in range(0, count_page*64, 64):
			try:
				tbody = get_data(get_html(f'https://hidemy.name/ru/proxy-list/?start={i}#list')).find('tbody')
				all_line = tbody.find_all('tr')
				for line in all_line:
					proxy = line.find_all('td')
					ip = proxy[0].text
					port = proxy[1].text
					writer(f'{ip}:{port}\n')
			except:
				print('error')
			a += 1
			sleep(5)
	except:
		print('pizdec, priexali')
	print('finish parse HIDEMYNAME')

def github():
	print('get start parse GITHUB')
	source = ['https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', 
		'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
		'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
		'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'
		'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
		'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
		'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
		'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
		'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt'
		]

	for url in source:
		try:
			writer(get_html(url))
			'''
			git_proxy = get_data(get_html(url))
			div = git_proxy.find('table').find_all('tr')
			for item in div:
				proxy_data = item.find_all('td')
				proxy = proxy_data[1].text
				writer(f'{proxy}\n')
			'''
		except:
			print(f'error git {url}')
			
	print('finish parse GITHUB')


reg = '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}:[0-9]{1,5})'


def regul():
    r = open('new_proxy.txt', 'r')
    lines = r.read()
    mass = re.findall(reg, lines)
    print(mass)

    for i in mass:
        os.system('echo ' + i + ' >> not_sort.txt')
        print(i)

    os.system('sort not_sort.txt | uniq > sort.txt')
    os.system('rm not_sort.txt')

def main():
	while True:
		rootjazz()
		github()
		# proxypedia()
		# hinky()
		# hidemyname()
		# htmlweb()
		regul()
		sleep(3600)

if __name__ == '__main__':
	main()