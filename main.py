# -------------- Day 48 --------------

from selenium import webdriver
from selenium.webdriver.common.by import By

# ----- keep Chrome browser open after program finishes ------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

# print(f"the price is {price_dollar}.{price_cents}")

# ------searching by name --------

search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# -------- searching by id ------
button = driver.find_element(By.ID, value="submit")
# print(button.size)

# -------searching by css selectors ----------
anchor_tag = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(anchor_tag.text)

# ------- searching by X-path ---------
by_x_path = driver.find_element(By.XPATH, value='//*[@id="container"]/li[7]/ul/li[3]')
# print(by_x_path.text)


#  ---------- search up coming events and print it by dictionary wise ---------
events_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# print(events_time)
# for time in events_time:
#     print(time.text)

events_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for name in events_name:
#     print(name.text)

events = {}

for n in range(len(events_time)):
    events[n] = {
        "time" : events_time[n].text,
        "name" : events_name[n].text,
    }

print(events)

# driver.close()    #for close single tab
driver.quit()   #for close all tab


