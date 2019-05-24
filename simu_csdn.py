from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome("/Users/dongheng/Downloads/chromedriver",chrome_options=chrome_options)
# driver.set_window_size(1024,7680)

driver.get("https://passport.csdn.net/login")
time.sleep(5)
driver.find_element_by_xpath('//div[@class="main-select"]//li[2]').click()
driver.find_element_by_name('all').send_keys("1041590182@qq.com")
driver.find_element_by_name('pwd').send_keys('efU-efg-n99-Nqp')
driver.find_element_by_xpath("//button[@data-type='account']").click()
time.sleep(10)
driver.save_screenshot("csdn.png")

driver.close()
