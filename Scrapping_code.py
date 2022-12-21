from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import requests
i = 0
c=0
import pandas as pd
#pandas
cols=['ID','ALT']
df = pd.DataFrame(columns=cols)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://pixabay.com/images/search/scenery/")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
for j in range(200):
 for k in range(300):
     ActionChains(driver).send_keys(Keys.END).perform()
 if i==0:
    img = driver.find_element_by_class_name('media_list')
 else:
     img = driver.find_element_by_class_name('external-media')
 p=img.find_elements_by_tag_name('img')
# p=driver.find_elements_by_tag_name('img')

 for post in p:
     i=i+1
     if i==2000:
         break
     src = post.get_attribute('src')
     name="download/captcha"+str(i)+".jpg"
     # r = requests.get(src)
     try:
      req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
      with open(name, "wb") as f:
          with urllib.request.urlopen(req) as r:
              f.write(r.read())
      df = df.append({'ID': name, 'ALT': str(post.get_attribute('alt'))},ignore_index=True)
      print(df)
     except:
         continue

 if c==0:
     driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div/a").click()
     c=1;
 else:
     driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div/a[2]").click()
print(i)
df.to_csv('records.csv')
driver.close()
