import json
import time

from config import TOKEN
# TOKEN = "your_anticapcha_token"

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def acp_api_send_request(driver, message_type, data={}):
	message = {
		'receiver': 'antiCaptchaPlugin',
		'type': message_type,
		**data
	}
	return driver.execute_script("""
	return window.postMessage({});
	""".format(json.dumps(message)))


def main():

	url = 'https://awmproxy.com/freeproxy.php'

	options = webdriver.ChromeOptions()
	browser = webdriver.Chrome('/home/kali/proxy/parser/main/chromedriver', options=options)

	browser.get('https://antcpt.com/blank.html')

	acp_api_send_request(
	    browser,
	    'setOptions',
	    {'options': {'antiCaptchaApiKey': TOKEN}}
	)
	print(acp_api_send_request)

	time.sleep(5)

	browser.get('https://awmproxy.com/freeproxy.php')

	time.sleep(5)

	browser.find_element_by_css_selector('input[type=submit]').click()

	time.sleep(10)

	browser.close()
	browser.quit()

if __name__ == '__main__':
	main()