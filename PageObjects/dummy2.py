import json
import time

# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from Utilities.BasePage import BasePage
#
# MY_GARAGE_LINK = (By.LINK_TEXT, 'My Garage')
# PAGE_NUMBER_BUTTONS = (By.XPATH, "//li[@role='presentation']")
# FIRST_PAGE_BUTTON = (By.XPATH, "//button[@id='slick-slide-control00' and @aria-selected='true']")
# CAR_DETAIL_TEXT = (By.CSS_SELECTOR, 'div#slick-slide00 h5')
# REMOVE_BUTTON = (By.CSS_SELECTOR, 'div#slick-slide00 div p a')
# REMOVE_ALL_BUTTON = (By.LINK_TEXT, 'Remove from watchlist')
# NEXT_BUTTON = (By.CSS_SELECTOR, 'span.watch-next')
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get('https://www.cargiant.co.uk/')
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, 'a.CallToActionPopupBlock__CallToActionLink-sc-1u8k8qw-0').click()
# driver.find_element(By.CSS_SELECTOR, 'a.sign-in-for-mygarage').click()
# driver.find_element(By.CSS_SELECTOR, 'input#PartialLogin_Username').send_keys('satdb_ec@yahoo.com')
# driver.find_element(By.CSS_SELECTOR, 'input#PartialLogin_Password').send_keys('password')
# #driver.find_element(By.CSS_SELECTOR, "input[value='Sign in']").click()
# driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "input[value='Sign in']"))
# time.sleep(4)
#
# # move to first page
# # while BasePage.is_visible(FIRST_PAGE_BUTTON):
# #     BasePage.do_click(NEXT_BUTTON)
# actual_watch_list = []
# no_of_pages = len(driver.find_elements_by_xpath("//li[@role='presentation']"))
# for i in range(no_of_pages):
#     #by_element = (By.CSS_SELECTOR, 'div#slick-slide0' + str(i) + ' h5')
#     print(i)
#     print(driver.find_element_by_css_selector('div#slick-slide0' + str(i) + ' h5').text)
#
#     actual_watch_list.append(driver.find_element_by_css_selector('div#slick-slide0' + str(i) + ' h5').text)
#     next_button = driver.find_element_by_css_selector('span.watch-next')
#     driver.execute_script("arguments[0].click();", next_button)
#     time.sleep(2)
#
# print(actual_watch_list)
#
# expected_watch_list = []
# with open('../Utilities/watchlist.txt', 'r') as file_handle:
#     car_list = json.load(file_handle)
#
# for i in range(len(car_list)):
#     if car_list[i][3] == 'Listed':
#         if car_list[i][4] == 'NOT SOLD':
#             l = list(car_list[i][2].split(", "))  # convert string to list, delimiter ', '
#             expected_watch_list.append(l[2:])   # remove the first two element of the list
# print(expected_watch_list)
#
list3 = []
list1 = ['Diesel, Black, 2016 (16), 64,151 miles', 'Diesel, Grey, 2016 (66), 20,834 miles', 'Petrol, Grey, 2016 (66), 34,075 miles', 'Petrol, White, 2017 (67), 23,240 miles']
list2 = [['Petrol', 'Grey', '2016 (66)', '34,075 miles'], ['Petrol', 'White', '2017 (67)', '23,240 miles'], ['Diesel', 'Grey', '2016 (66)', '20,834 miles']]

for i in range(len(list1)):
    print(list1[i])
    list3.append(list(list1[i].split(", ")))
print(list3)

with open('../Utilities/cars.JSON') as file:
    data = json.load(file)
