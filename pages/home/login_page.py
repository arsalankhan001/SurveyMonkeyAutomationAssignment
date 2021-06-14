from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
from selenium.webdriver.support.select import Select
import logging
import time


class loginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    # locators

    _loginLink = "//a[contains(text(),'Log in')]"
    _user_name = "username"
    _password = "password"
    _login_Button = "//button[@class='wds-button wds-button--stretch wds-button--icon-right wds-button--arrow-right' " \
                    "and contains(text(),'LOG IN')] "
    _create_survey = "//div[@id='hd']//a[@class='create-survey alt btn SL_split']"
    _create_survey_ = "//a[@class='create-survey alt btn SL_split' and contains(text(),'CREATE SURVEY')]"
    startfromscratchButton = "//button[contains(text(), 'Start from scratch')]"
    _survey_name = "surveyTitle"
    _survey_catagory = "//div[@class='wds-select wds-select--stretched wds-select--md " \
                       "sm-new-survey-modal--select']/select "
    _create_new_survey = "newSurvey"
    _page_title = "//div[@class='page-title-container page-title-container-v3 clearfix']//span[@class='page-title " \
                  "user-generated empty wds-button wds-button--ghost-filled wds-button--sm'] "
    _page_title_click = "//div[@class='page-title-container page-title-container-v3 clearfix']//span[" \
                        "@class='page-title " \
                        "user-generated empty wds-button wds-button--ghost-filled wds-button--sm'] "

    _page_title_textbox = "pageTitle"
    _page_sub_title = "pageSubtitle"
    _save_title_button = "//form[@id='pageTitleForm']//a[@class='wds-button wds-button--sm save' and contains(text(),'SAVE')]"

    # Drop down button
    _multiple_choices_drop_down = "changeQType"

    # First question
    _question_box = "editTitle"
    _single_text_box_option = "//a[@class='option add-q-item']//span[@class='listText' and contains(text(),'Single Textbox')]"

    # second question
    second_q_box = "editTitle"
    # second_q_box = "//div[@class='rteToolbarContainer title-rte-container empty']//span[@class='placeholder'][" \
    # "normalize-space()='Enter your question']"
    # _multiple_choice_option = "//a[@class='option add-q-item selected']//span[@class='listText' and contains(text(),'Multiple Choice')]"
    _multiple_choice_option = "//body[@id='create']/ul//ul[@class='add-q-menu-left']/li[1]/div/a[@href='#']/span[@class='listText']"
    _enter_first_choice = "//table[@id='rows']//div[@class='rte input mce-content-body']"
    _enter_second_choice = "//table[@id='rows']//div[@class='rte input mce-content-body mce-edit-focus']"
    _enter_third_choice = "//table[@id='rows']//child::tr[6]//child::td[2]"
    j_enter_first_choice = "//tbody/tr[4]/td[2]/div/div[1]"
    j_enter_second_choice = "//tbody/tr[5]/td[2]/div/div[1]"
    j_enter_third_choice = "//tbody/tr[6]/td[2]/div/div[1]"

    # third question
    _date_time = "//a[@class='option add-q-item']//span[@class='listText' and contains(text(),'Date / Time')]"
    _date_time_inputbox = "//table[@id='rows']//div[@class='rte input notranslate mce-content-body mce-edit-focus']"
    j_date_time_ = "//body[@id='create']/ul/li/ul[2]/li[7]/div/a"


    # Fourth question
    _drop_down_option = "//a[@class='option add-q-item selected']//span[@class='listText' and contains(text(),'Dropdown')]"
    _select_type_option = "answerBankCategorySelect"
    # is k baad drop down wale function se select kr k 4th inder yes no clik krna h

    # fifth question

    # next question button
    _next_question_button = "//div[@class='buttons']//a[@class='wds-button wds-button--sm wds-button--icon-left add-another' and contains(text(),'NEXT QUESTION')]"



    # sixth question
    check_box_question_bank = "//tbody/tr[4]/td[2]/div/div[1]"
    check_box_theme = "//tbody/tr[5]/td[2]/div/div[1]"
    check_box_graphic = "//tbody/tr[6]/td[2]/div/div[1]"
    check_box_template = "//tbody/tr[7]/td[2]/div/div[1]"
    check_box_collector = "//tbody/tr[8]/td[2]/div/div[1]"


    # seventh Question
    _service_lable = "//table[@id='rows']//child::tbody//child::tr[3]//child::td[1]//child::div[1]//child::div[1]"
    _support_lable = "//table[@id='rows']//child::tbody//child::tr[4]//child::td[1]//child::div[1]//child::div[1]"
    _responsiveness_lable = "//table[@id='rows']//child::tbody//child::tr[5]//child::td[1]//child::div[1]//child::div[1]"
    _rating_veryVgood_ = "//tbody[@class='columnSetting singleLine']//child::tr[2]//child::td[1]//child::div[1]//child::div[1]"
    _rating_very_good = "//tbody[@class='columnSetting singleLine']//child::tr[2]//child::td[1]//child::div[1]//child::span[@class='placeholder']"
    _rating_good = "//tbody[@class='columnSetting singleLine']//child::tr[3]//child::td[1]//child::div[1]//child::div[1]"
    _rating_avrage = "//tbody[@class='columnSetting singleLine']//child::tr[4]//child::td[1]//child::div[1]//child::div[1]"
    _rating_below_avrage = "//tbody[@class='columnSetting singleLine']//child::tr[5]//child::td[1]//child::div[1]//child::div[1]"

    # DONE button
    _done_button = "//button[@class='wds-button wds-button--sm survey-page-button done-button notranslate' and contains(text(),'DONE')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickLoginLink(self):
        self.elementClick(self._loginLink, locatorType="xpath")

    def sendUsername(self, username):
        self.sendKeys(username, self._user_name)

    def sendPassword(self, password):
        self.sendKeys(password, self._password)

    def clickLoginButton(self):
        self.elementClick(self._login_Button, locatorType="xpath")

    def createSurvey(self):
        self.elementClick(self._create_survey, locatorType="xpath")

    def startfromscratch(self):
        self.elementClick(self.startfromscratchButton, locatorType="xpath")

    def sendName(self, name):
        self.sendKeys(name, self._survey_name)

    def catagory(self, data):
        self.dropDown(data, self._survey_catagory)

    def creatNewSurvey(self):
        self.elementClick(self._create_new_survey)

    def survey(self):
        self.sendName("Bitcoin")
        element = self.driver.find_element_by_xpath(self._survey_catagory)
        sel = Select(element)
        sel.select_by_index(5)
        self.creatNewSurvey()

    def pagetitleclick(self):
        self.elementClick(self._page_title_click, locatorType="xpath")
        self.sendKeys("cryptocurrency", self._page_title_textbox)
        self.sendKeys("this survey is about cryptocurrency", self._page_sub_title)
        self.elementClick(self._save_title_button, locatorType="xpath")

    def firstQuestion(self):
        self.elementClick(self._multiple_choices_drop_down)
        self.elementClick(self._single_text_box_option, locatorType="xpath")
        self.waitForElement(self._question_box)
        self.sendKeys("enter your email", self._question_box)
        self.waitForElement(self._next_question_button, locatorType="xpath")
        self.elementClick(self._next_question_button, locatorType="xpath")
        time.sleep(10)

    def secondQuestion(self):
        self.sendKeys("how offen do you use server monkey", self._question_box)
        time.sleep(5)
        self.waitForElement(self._multiple_choices_drop_down, locatorType="xpath")
        self.elementClick(self._multiple_choices_drop_down)
        self.elementClick(self._multiple_choice_option, locatorType="xpath")
        # time.sleep(10)
        self.sendKeys("Regularly", self.j_enter_first_choice, locatorType="xpath")
        self.sendKeys("Sometimes", self.j_enter_second_choice, locatorType="xpath")
        self.sendKeys("Never tried", self.j_enter_third_choice, locatorType="xpath")
        self.elementClick(self._next_question_button, locatorType="xpath")

    def thirdQuestion(self):
        self.waitForElement(self._question_box)
        self.sendKeys("From when you are using ServerMonkey?", self._question_box)
        self.elementClick(self._multiple_choices_drop_down)
        self.elementClick(self.j_date_time_, locatorType="xpath")
        self.elementClick(self._next_question_button, locatorType="xpath")

    def fouthQuestion(self):
        time.sleep(8)
        self.sendKeys("How will rate the ease of survey creation?", self._question_box, )
        self.waitForElement(self._next_question_button, locatorType="xpath")
        self.elementClick(self._next_question_button, locatorType="xpath")
        time.sleep(4)

    def fifthQuestion(self):
        time.sleep(10)
        self.sendKeys("Did you get meaningful data from survey analysis?", self._question_box)
        time.sleep(8)
        # self.elementClick(self._select_type_option)
        element = self.driver.find_element_by_id(self._select_type_option)
        sel = Select(element)
        sel.select_by_index(3)
        time.sleep(10)
        self.elementClick(self._next_question_button, locatorType="xpath")
        time.sleep(5)

    def sixthQuestion(self):
        time.sleep(10)
        self.sendKeys(" Check the Features you like about SurveyMonkey?", self._question_box)
        time.sleep(7)
        self.sendKeys("Question bank", self.check_box_question_bank, locatorType="xpath")
        self.sendKeys("Themes", self.check_box_theme, locatorType="xpath")
        self.sendKeys("Graphical Result", self.check_box_graphic, locatorType="xpath")
        # self.elementClick(self.plus_sign_add_check_box, locatorType="xpath")
        self.sendKeys("Template Re-usability", self.check_box_template, locatorType="xpath")
        self.sendKeys("Collectors", self.check_box_collector, locatorType="xpath")
        self.elementClick(self._next_question_button, locatorType="xpath")

    def seventhQuestion(self):
        self.waitForElement(self._question_box)
        self.sendKeys("Rate our features.", self._question_box)
        time.sleep(8)
        self.waitForElement(self._service_lable, locatorType="xpath")
        time.sleep(5)
        self.sendKeys("Service", self._service_lable, locatorType="xpath")
        self.sendKeys("Support", self._support_lable, locatorType="xpath")
        time.sleep(5)
        self.sendKeys("Responsiveness", self._responsiveness_lable, locatorType="xpath")
        self.sendKeys("Very Good", self._rating_veryVgood_, locatorType="xpath")
        time.sleep(5)
        self.sendKeys("Good", self._rating_good, locatorType="xpath")
        self.sendKeys("Average", self._rating_avrage, locatorType="xpath")
        time.sleep(5)
        self.sendKeys("Below Average", self._rating_below_avrage, locatorType="xpath")
        self.elementClick(self._next_question_button, locatorType="xpath")
        time.sleep(10)

    def eightQuestion(self):
        time.sleep(10)
        self.elementClick(self._multiple_choices_drop_down)
        self.elementClick(self._single_text_box_option, locatorType="xpath")
        self.waitForElement(self._question_box)
        self.sendKeys("List the features you like most.", self._question_box)
        self.waitForElement(self._next_question_button, locatorType="xpath")
        self.elementClick(self._next_question_button, locatorType="xpath")

    def ninthQuestion(self):
        time.sleep(10)
        self.waitForElement(self._question_box)
        self.sendKeys("Will recommend SurveyMonkey to your friends / Colleagues?", self._question_box)
        time.sleep(8)
        element = self.driver.find_element_by_id(self._select_type_option)
        sel = Select(element)
        sel.select_by_index(3)
        time.sleep(10)
        self.elementClick(self._next_question_button, locatorType="xpath")

    def tenthQuestion(self):
        time.sleep(10)
        self.waitForElement(self._question_box)
        self.sendKeys("Comments / Feedback", self._question_box)


    def doneButton(self):
        time.sleep(10)
        self.elementClick(self._done_button, locatorType="xpath")

    def login(self, username="", password=""):
        self.clickLoginLink()
        self.sendUsername(username)
        self.sendPassword(password)
        self.clickLoginButton()
        self.createSurvey()
        self.startfromscratch()
        self.survey()
        self.pagetitleclick()
        self.firstQuestion()
        self.secondQuestion()
        self.thirdQuestion()
        self.fouthQuestion()
        self.fifthQuestion()
        self.sixthQuestion()
        self.seventhQuestion()
        self.eightQuestion()
        self.ninthQuestion()
        self.tenthQuestion()
        self.doneButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//a[@class='create-survey alt btn SL_split' and contains(text(),'CREATE "
                                       "SURVEY')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//li[text()='The username or password you entered is incorrect. Please try "
                                       "again--and remember that passwords are case sensitive.']",
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._user_name)
        emailField.clear()
        passwordField = self.getElement(locator=self._password)
        passwordField.clear()
