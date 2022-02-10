import random
from selenium.webdriver import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/alilie/Desktop/Website_automation/chromedriver')
driver.get("http://tutorialsninja.com/demo/")
driver.maximize_window()

phones = driver.find_element_by_xpath("//a[text()='Phones & PDAs']")
phones.click()

iphone = driver.find_element_by_xpath("//a[text()='iPhone']")
iphone.click()
time.sleep(1)

first_pic = driver.find_element_by_xpath("//img[@src='http://tutorialsninja.com/demo/image/cache/catalog/demo/iphone_1-228x228.jpg']")
first_pic.click()

for i in range(5):
    next_click = driver.find_element_by_xpath("//button[@title='Next (Right arrow key)']")
    next_click.click()
    time.sleep(2)

driver.save_screenshot('screenshot#'+str(random.randint(1,5))+'.png')

close = driver.find_element_by_xpath("//button[@title='Close (Esc)']")
close.click()
time.sleep(1)

quantity = driver.find_element_by_id("input-quantity")
quantity.click()
quantity.clear()
quantity.send_keys("2")

add_cart = driver.find_element_by_id("button-cart")
#add_cart.click()

#perform mouseover
laptops = driver.find_element_by_xpath("//a[text()='Laptops & Notebooks']")
action =ActionChains(driver)
action.move_to_element(laptops).perform()

laptops2=driver.find_element_by_xpath("//a[text()='Show All Laptops & Notebooks']")
laptops2.click()
time.sleep(1)

hp_laptop = driver.find_element_by_xpath("//a[text()='HP LP3065']")
hp_laptop.click()
time.sleep(1)

add_to_chart = driver.find_element_by_xpath("//button[text()='Add to Cart']")
add_to_chart.location_once_scrolled_into_view#scorl pana cand elementul devine primul element de pe ecranul afisat
time.sleep(1)

calendar = driver.find_element_by_xpath("//span[@class='input-group-btn']/button[@class='btn btn-default' and @type='button']")
calendar.click()

date = driver.find_element_by_id("input-option225")
date.clear()
date.send_keys("2022-12-24")
time.sleep(1)

add_to_chart2 = driver.find_element_by_id("button-cart")
add_to_chart2.click()
time.sleep(1)

#checkout = driver.find_element_by_xpath("//a[@href='http://tutorialsninja.com/demo/index.php?route=checkout/checkout']").click()
checkout = driver.find_element_by_xpath("//a[@title='Checkout']/i[@class='fa fa-share']").click()
time.sleep(1)

guest_ckout = driver.find_element_by_xpath("//input[@type='radio' and @value='guest']").click()
time.sleep(1)
continue_button = driver.find_element_by_id("button-account").click()

down = driver.find_element_by_xpath("//a[@data-toggle='collapse' and @aria-expanded='true']")
down.location_once_scrolled_into_view

time.sleep(5)#implicit wait

first_name = driver.find_element_by_id("input-payment-firstname").send_keys("Ilie")
last_name = driver.find_element_by_id("input-payment-lastname").send_keys("Alex")
email = driver.find_element_by_id("input-payment-email").send_keys("ai@gmail.com")
telephone = driver.find_element_by_id("input-payment-telephone").send_keys("0732851923")
address = driver.find_element_by_id("input-payment-address-1").send_keys("Intarea Badeni")
city = driver.find_element_by_id("input-payment-city").send_keys("Bucharest")
postal_code = driver.find_element_by_id("input-payment-postcode").send_keys("030472")
#dropdown
country = driver.find_element_by_id("input-payment-country")
dropdown = Select(country)
dropdown.select_by_visible_text("Romania")#al 87 element din dropdown

time.sleep(2)

region = driver.find_element_by_id("input-payment-zone")
region = Select(region)
region.select_by_index(2)

time.sleep(2)
continue_2 = driver.find_element_by_xpath("//input[@id='button-guest']").click()

time.sleep(2)
continue_3 = driver.find_element_by_id("button-shipping-method").click()
time.sleep(2)
agree = driver.find_element_by_xpath("//input[@type='checkbox' and @name='agree']").click()
time.sleep(2)
continue_4 = driver.find_element_by_id("button-payment-method").click()
time.sleep(1)
price = driver.find_element_by_xpath("//table[@class='table table-bordered table-hover']/tfoot/tr[3]/td[2]")
print(price.text)
assert int(price.text[1:-3]) >= 50, "price lower than 50 USD"
time.sleep(1)
continue_6 = driver.find_element_by_id("button-confirm").click()
time.sleep(1)
continue_7 = driver.find_element_by_xpath("//a[@class='btn btn-primary']").click()
time.sleep(10)

#driver.close()