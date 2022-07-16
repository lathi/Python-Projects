from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/harshitlathi/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# driver.get("http://secure-retreat-92358.herokuapp.com/")

# count = driver.find_element_by_css_selector("#articlecount a")
# count.click()

# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("NERC")
# search_bar.send_keys(Keys.ENTER)

# fname = driver.find_element_by_name("fName")
# fname.send_keys("Harshit")
#
# lname = driver.find_element_by_name("lName")
# lname.send_keys("Lathi")
#
# email = driver.find_element_by_name("email")
# email.send_keys("harshitlathi18@gmail.com")
#
# button = driver.find_element_by_css_selector("button")
# button.send_keys(Keys.ENTER)

# driver.get("https://www.appbrewery.co/p/newsletter")
# email = driver.find_element_by_id("member_email")
# email.send_keys("harshitlathi@gmail.com")
# email.send_keys(Keys.ENTER)

def check_which_item_to_buy():
    for item in market_items:
        if my_cookies_count > int(market_items[item]['price']):
            continue
        else:
            return item - 1


driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

market = driver.find_elements_by_css_selector("#store div")

market_items = {}
count = 0
for item1 in market:
    # print(item.get_attribute("id"))
    item = item1.find_elements_by_css_selector("b")
    # print(f"{item[0].text}\n")
    market_items[count] = {
        'itemID': item1.get_attribute("id"),
        'price': item[0].text.split(" ")[-1].replace(",", "")
    }
    count += 1

timeout = time.time() + 5
five_min = time.time() + 60 * 5
counter = 1

while True:
    cookie.click()

    if time.time() > timeout:
        my_cookies = driver.find_element_by_id("money")
        my_cookies_count = int(my_cookies.text.replace(",", ""))
        buy_item = driver.find_element_by_id(market_items[check_which_item_to_buy()]["itemID"])
        buy_item.click()
        counter += .25
        timeout = time.time() + 5 * counter

    if time.time() > five_min:
        cps = driver.find_element_by_id("cps")
        print(cps.text)
        break
