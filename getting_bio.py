import json
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ekhon json file ta load kore sobar profile e jabo ar bio collect korbo

options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url_oo = "https://mbasic.facebook.com"
driver.maximize_window()
driver.get(url_oo)

with open("crd.json", "r") as credentials:
    data = json.load(credentials)

email = driver.find_element_by_id("m_login_email")
email.send_keys(data["username"])
password = driver.find_element_by_xpath("//input [@name='pass']")
password.send_keys(data["pass"])
login = driver.find_element_by_xpath("//input [@name='login']").click()


# login complete


with open("Sample.json", "r", encoding="utf-8") as read_it:
    data = json.load(read_it)


# profile theke bio anar function
# NOTE to make the code run faster change this value
wait = random.randint(20, 40)


def bio_collector(url):
    try:
        driver.get(url)
        try:
            bio = driver.find_element_by_xpath(
                '//*[@id="m-timeline-cover-section"]/div[2]/div[2]'
            ).text
        except:
            bio = "Bio Nai"
    except:
        print("Bio Extracting Failed", url)
        bio = None
    print(f" Waiting for {wait} seconds -----")
    time.sleep(wait)
    return bio


count = 1
for i in data:
    if i["bio"] == None:
        print(
            f' Bio collected of {i["index"]}: {i["name"]} ...',
        )
        i["bio"] = str(bio_collector(i["url_i"]))

    else:
        print(f'{i["name"]} - bio done')
    # updation of database
    a_file = open("Sample.json", "w", encoding="utf-8")
    json.dump(data, a_file)
    a_file.close()

driver.quit()
