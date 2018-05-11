from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get("https://www.expresslanes.com/historic-rates")

def helper(hour, min, visited):
    browser.find_element_by_id("trip-date").click()
    prev = browser.find_element_by_xpath("//span[./text()='Prev']")
    prev.click()
    calender = browser.find_element_by_xpath("//a[./text() ='12']")
    calender.click()
    if visited ==0:
    #hour slidebar
        slidebar = browser.find_element_by_id("ui_tpicker_hour_tripdate")
        width = slidebar.size['width']
        move = ActionChains(browser)
        slider = browser.find_element_by_xpath("//dd[@id='ui_tpicker_hour_tripdate']/a")
        move.click_and_hold(slider).move_by_offset(hour, 0).release().perform()

    #minute siderbar
    minute_move = ActionChains(browser)
    minute_slidebar = browser.find_element_by_id("ui_tpicker_minute_tripdate")
    minute_width = minute_slidebar.size['width']
    minute_slider = browser.find_element_by_xpath("//dd[@id='ui_tpicker_minute_tripdate']/a")
    minute_move.click_and_hold(minute_slider).move_by_offset(min,0).release().perform()

    #click done button for calender
    browser.find_element_by_class_name("ui-datepicker-close").click()

    if visited ==0:
        direction = browser.find_element_by_class_name("chosen-single")
        direction.click()
        choose_n_or_s  = browser.find_element_by_xpath("//li[./text() = 'Southbound']")
        choose_n_or_s.click()

        starting_point = browser.find_element_by_id("entryPtSel_chosen")
        starting_point.click()



        starting_road = browser.find_element_by_xpath("//li[./text() = '495 Express Lanes/I-495/I-95']")
        starting_road.click()

        browser.find_element_by_id("exitPtSel_chosen").click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[./text() = 'I-95 Near Dale Boulevard']"))).click()

    browser.find_element_by_id("btn-rate").click()
    time.sleep(15) #Explicit wait


    ee =browser.find_element_by_xpath("//span[@class='rate']")
    print(str(hour) + ":" + str(min) + " = " + str(ee.text))


def help(ho, mi):
	print(ho)
	print(mi)

for h in range(0,10):
    browser.refresh()
    minu = 0

    hr = 110+h*5
    first = 0

    for m in range(0,6):
        if m != 0:
            minu = 32+1
        helper(hr,minu, first)
        if first == 0:
            first = 1
