from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

loginpath = "//a[contains(text(),'Log in')]"
usernameid = "username"
password = "password"
loginbtn = "//div[@id='navbar-inverse-collapse']/div//a[@href='/login']"
loginbtn2 = "//button[@class='wds-button wds-button--stretch wds-button--icon-right wds-button--arrow-right' and " \
            "contains(text(),'LOG IN')] "
createsurvey = "//div[@id='hd']//a[@class='create-survey alt btn SL_split']"
crossbutton = "//button[@class='wds-button wds-button--primary wds-button--solid wds-button--md wds-button--icon-only " \
              "sm-base-question__close'] "
sidestartfromscratch = "//button[contains(text(), 'Start from scratch')]"
survey_catagory = "//div[@class='wds-select wds-select--stretched wds-select--md sm-new-survey-modal--select']/select"

_survey_name = "surveyTitle"
_create_new_survey = "newSurvey"
_page_title_click = "//div[@class='page-title-container page-title-container-v3 clearfix']//span[@class='page-title " \
                    "user-generated empty wds-button wds-button--ghost-filled wds-button--sm'] "

_page_title_checkbox = "pageTitle"
_page_sub_title = "pageSubtitle"
_multiple_choices_drop_down = "//span[@class='qType' and contains(text(),'Multiple Choice')]"
_single_text_box_option = "//a[@class='option add-q-item']//span[@class='listText' and contains(text(),'Single " \
                          "Textbox')] "

_save_title_button = "//form[@id='surveyTitleForm']//a[text()='SAVE']"


first_q_box = "//div[@class='rteToolbarContainer title-rte-container empty']"

second_q_box = "//div[@class='rteToolbarContainer title-rte-container empty']//span[@class='placeholder'][" \
               "normalize-space()='Enter your question'] "
class login:

    def clickOnLogin(self):
        baseurl = "https://www.surveymonkey.com"
        driver = webdriver.Chrome()

        # maximise window
        driver.maximize_window()
        driver.implicitly_wait(10)

        # open Url
        driver.get(baseurl)
        driver.find_element_by_xpath(loginpath).click()
        time.sleep(10)
        username = driver.find_element(By.ID, usernameid)
        username.send_keys("arsalan.khan01")
        password1 = driver.find_element(By.ID, password)
        password1.send_keys("arsalan.123")
        time.sleep(10)
        driver.find_element_by_xpath(loginbtn2).click()
        print("login")
        driver.find_element(By.XPATH, createsurvey).click()
        time.sleep(10)
        driver.find_element(By.XPATH, sidestartfromscratch).click()
        time.sleep(10)
        driver.find_element_by_id(_survey_name).send_keys("bitcoin")
        time.sleep(10)
        element = driver.find_element_by_xpath(survey_catagory)
        sel = Select(element)
        sel.select_by_value("5")
        time.sleep(8)
        driver.find_element_by_id(_create_new_survey).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(_page_title_click).click()


ff = login()
ff.clickOnLogin()
