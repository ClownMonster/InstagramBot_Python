from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.instagram.com')
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys('clownmonster000@gmail.com')
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys('')
driver.find_element_by_xpath('//button[@type = "submit"]').click()
sleep(4)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
sleep(2)



def get_followers_list():
    global driver
    driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
    sleep(2)
    last_ht, ht = 0,1
    scroll_box = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
    while last_ht != ht:
        last_ht = ht
        sleep(1)
        ht = driver.execute_script('''
         argument[0].scrollTo(0, argument[0].scrollHeight);
         return argument[0].scrollHeight
         ''',scroll_box)

    links = scroll_box.find_element_by_tag_name('a')
    print(links)
    names = [name.text for name in links if name != '' ]
    print(names)

get_followers_list()
