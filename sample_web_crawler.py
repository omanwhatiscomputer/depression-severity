# -*- coding: utf-8 -*-
# 24 March 2021 2:45 pm +0600 GMT
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

file = open('test.txt', 'a+', encoding='utf-8')


#file_csv = open('dataset.csv', 'w', encoding='utf-8')
#csv_write = csv.writer(file_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


PATH = 'C:\Program Files (x86)\chromedriver.exe'

page_number = 1
total_pages = 4
for i in range(total_pages):
    print(f'https://dev.maya.com.bd/questions/tag/123?page={page_number}')
    driver = webdriver.Chrome(PATH)
    driver.get(f'https://dev.maya.com.bd/questions/tag/123?page={page_number}')
    
    try:
        body = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        q_class = body.find_elements_by_class_name('question-dr')
        q_posts = [x.text for x in q_class]
    except:
        file.close()
    finally:
        for i in range(len(q_posts)):
            if i%2 == 0:
                #print(q_posts[i]+'\n')
                file.write(q_posts[i]+'\n')
                #csv_write.writerow([q_posts[i]])
        #driver.find_elements_by_tag_name('b')
        driver.quit()
        
    page_number += 1

file.close()