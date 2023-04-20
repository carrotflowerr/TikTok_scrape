import time
import re
from selenium import webdriver



user = str(input())


driver = webdriver.Chrome('/sbin/chromedriver')
driver.get('https://www.tiktok.com/'+str(user))

time.sleep(5)
driver.refresh()

time.sleep(5)
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    
    if new_height == last_height:
        break
    
    last_height = new_height
    
    # Wait for 30 seconds to see if there's any additional videos
    time.sleep(5)
    
page_source = driver.page_source
video_urls = re.findall(r'https://www.tiktok.com/'+str(user)+'/video/[^"]+', page_source)

print(video_urls)
driver.quit()
