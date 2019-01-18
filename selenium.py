from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import datetime

if __name__ == '__main__':
    caps = webdriver.DesiredCapabilities().FIREFOX
    caps["marionette"] = True

    binary = FirefoxBinary(r'H:\Mozilla Firefox\firefox.exe')

    fp = webdriver.FirefoxProfile()
    fp.set_preference("permissions.default.image",2)

    driver = webdriver.Firefox(firefox_binary=binary,capabilities=caps,firefox_profile=fp)

    driver.get("https://movie.douban.com/top250")

    f = open('douban.txt','w',encoding='utf-8')
    f.write(str(datetime.datetime.now())+'\n')
    movies = []
    for page in range(1,11):
        commment = driver.find_elements_by_xpath("//div[@class='hd']")
        for each in commment:
            content = each.find_element_by_tag_name('span')
            #print(content.text.strip())
            movies.append(content.text.strip())
        try:
            next_page = driver.find_element_by_xpath("//a[@href='?start=" +str(page*25)+"&filter=']")
            next_page.click()
        except:
            break
    for movie in movies:
        f.write(movie+'\n')

    f.write(str(datetime.datetime.now()) + '\n')
    f.close()



