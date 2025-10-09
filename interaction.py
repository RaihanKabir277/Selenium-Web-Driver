from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# active_editors = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # print(active_editors.text)
# # active_editors.click()

# editors_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# # print(editors_articles.text)

# ---------- scrap link by link_test ---------
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# ------- search automatically sending keyboard input to Selenium --------

# search1 = driver.find_element(By.NAME, value="search")
# # search1.send_keys("Python")
# # search1.send_keys(Keys.ENTER)
# search1.send_keys("Python", Keys.ENTER)



driver.quit()
