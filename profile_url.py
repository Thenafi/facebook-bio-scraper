import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ekahne just profile e login kore sobar friends page the sobar name ar url collect  kore
# ekta jason database type banailam


# at first lets login
# need these bugichugi & dont care about this
# if you really wanna know google it
options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# now going to the website
url_oo = "https://mbasic.facebook.com"
driver.maximize_window()
driver.get(url_oo)
# login koram
with open("crd.json", "r") as credentials:
    data = json.load(credentials)


email = driver.find_element_by_id("m_login_email")
email.send_keys(data["username"])
password = driver.find_element_by_xpath("//input [@name='pass']")
password.send_keys(data["pass"])
login = driver.find_element_by_xpath("//input [@name='login']").click()

# ind mane index for our friends
ind = 0
all_friends = []  # sob data ene dhukamu


# ebar amora profile e dhukbo and tar por friends er list e jabo
driver.get("https://mbasic.facebook.com/profile.php")
friends_list = driver.find_element_by_link_text("Friends").click()
print(driver.current_url)
# uprer print ta just for testing purpose


# now name ar sobar url collect korbo

# eta hocche first page er jonno 2nd page gele while diya arekta function loop kortesi..
# bcz facebook diffrent page e different element render kore
# ei ta dhorte amar life er 2 hour waste hoise .
# b****** facebook
friends = driver.find_elements_by_xpath(
    '//a[@class="ch"]'
)  # main jadu eta ..eitay amaro html element khuje ber kori xpath diya
for i in friends:
    name_of_friend = i.text
    url = i.get_attribute("href")
    friend = {"index": ind, "name": name_of_friend, "url_i": url, "bio": None}
    ind += 1
    all_friends.append(friend)

# 2nd pager er jonno diffrent jinish
def finding_namesandurls_2nd():
    print(len(all_friends))
    global ind
    friends = driver.find_elements_by_xpath('//a[@class="bs"]')
    for i in friends:
        name_of_friend = i.text
        url = i.get_attribute("href")
        friend = {"index": ind, "name": name_of_friend, "url_i": url, "bio": None}
        ind = ind + 1
        all_friends.append(friend)


# looping through all the friends
while True:
    try:
        looking_for_another_page_of_friends = driver.find_element_by_link_text(
            "See More Friends"
        )
        looking_for_another_page_of_friends.click()
    except:
        print("page over")
        break
    finding_namesandurls_2nd()


driver.quit()

with open("Sample.json", "w", encoding="utf-8") as p:
    json.dump(all_friends, p)


# btw there is lotof space for refinig and refactoring . go on if you wish do it
