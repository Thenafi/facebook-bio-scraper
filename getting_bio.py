from ast import Try
import json
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ekhon json file ta load kore sobar profile e jabo ar bio collect korbo
def bio():
    options = Options()
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    url_oo = "https://mbasic.facebook.com"
    driver.maximize_window()
    driver.get(url_oo)

    with open("credentials.json", "r") as credentials:
        data = json.load(credentials)

    email = driver.find_element_by_id("m_login_email")
    email.send_keys(data["username"])
    password = driver.find_element_by_xpath("//input [@name='pass']")
    password.send_keys(data["pass"])
    login = driver.find_element_by_xpath("//input [@name='login']").click()

    # login complete

    with open("output.json", "r", encoding="utf-8") as read_it:
        data = json.load(read_it)

    # profile theke bio anar function

    def bio_collector(url):
        try:
            driver.get(url)
            try:
                driver.find_element_by_xpath(
                    """//h2[contains(text(),"You Can't Use This Feature Right Now")]"""
                )
                print("You are blocked. Try later and increase the delay")
                return "blocked"
            except:
                try:
                    bio = driver.find_element_by_xpath(
                        '//*[@id="m-timeline-cover-section"]/div[2]/div[2]'
                    ).text
                except:
                    bio = "Bio Nai"
        except:
            print("Bio Extracting Failed", url)
            bio = None
        ##########################
        #  to make the code run faster change these value
        # example (0,19)/ (10,15)
        wait = random.randint(15, 25)
        print(f" Waiting for {wait} seconds -----")
        time.sleep(wait)
        return bio

    count = 1
    for i in data:
        if i["bio"] == None:
            print(
                f' Bio collected of {i["index"]}: {i["name"]} ...',
            )
            info = bio_collector(i["url_i"])
            if info == "blocked":
                break
            else:
                i["bio"] = str(info)

        else:
            print(f'{i["name"]} - bio done')
        # updation of database
        if data is not None:
            a_file = open("output.json", "w", encoding="utf-8")
            json.dump(data, a_file)
            a_file.close()
        else:
            pass

    driver.quit()


if __name__ == "__main__":
    print("Run main.py file")
