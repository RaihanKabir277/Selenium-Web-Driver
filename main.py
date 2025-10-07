# -------------- Day 48 --------------

from selenium import webdriver

# ----- keep Chrome browser open after program finishes ------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")


# driver.close()    #for close single tab
# driver.quit()   #for close all tab


