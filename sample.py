import requests
import bs4
import fake_useragent

def main():

	url = 'https://premproxy.com/list/ip-port/4.htm'

	user = fake_useragent.UserAgent().random
	headers = {
		'user-agent': user
	}

	r = requests.get(url, headers=headers)
	print(r.text)


if __name__ == '__main__':
	main()