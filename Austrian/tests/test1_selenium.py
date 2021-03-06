from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("https://book.austrian.com/app/fb.fly?pos=BY&l=en")

# the page is ajaxy so the title is originally this:
#print driver.title

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("/html/body/div[1]/div[4]/div[3]/div[3]/div[2]/div[1]/form/div[2]/div/div[7]/div/div[2]/div/div/div/div/button[1]")

# type in the search
inputElement.click()

# submit the form (although google automatically searches now without submitting)
#inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("0"))

    # You should see "cheese! - Google Search"
    print(driver.find_element_by_name("/html/body/div[1]/div[4]/div[3]/div[3]/div[2]/div[1]/form/div[2]/div/div[7]/div/div[2]/div/div/div/div/button[1]")
)

finally:
    driver.quit()
