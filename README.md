## **Facebook Scraper🕷**

It's a selenium-based script which scrapes/collects all the bios of your Facebook friends👼.
Frist it collects the URL and visit those pages one by one to get the bio.

It saves all the data in an output.json file and acts as a database. There is a converter file to convert the data into excel or csv format

For some Facebook's Limitation the script runs slow. But there's instructions (in main.py or below) to make it faster.
The script can be stopped and resumed as many times as required because it might take a long time to collect all bios.
So, my suggestion is to run it multiple times a day if you wish to scrape all your friends🙄.
For me, the first 300-400 friends were enough 😋

---

**Usages**

First create _credentials.json_ file and add your Facebook Credentials in it like this

```
{
"username":  "username",
"pass":  "password"
}
```

Recommended to use virtual environment. You can read [here.](https://dev.to/ngazetungue/python-script-in-virtual-environment-beginners-guide-h6d)

Activate your virtual environment or just run these.

First install the required packages

    pip install -r "requirements.txt"

then

    python main.py

Thats it 🥰 Watch and enjoy the scraping.

---

**Instructions to Scrape Faster**

Change the random integer variable at line 37 of getting_bio.py file.

    wait  =  random.randint(20,  40)

It's the delay between each profile visit. Visiting profile like a bot (too fast) causes the block.

---

**_NOTEs_**

- You should have python installed
- You should have chrome in your machine
- Built on windows and tested on windows
- _This is a beginner level code, and this might need some refactoring. But it works._
- there might be some unrecognizable comments for non-bengali coders
- there's zero to none error handling.
- add issues if you find any
