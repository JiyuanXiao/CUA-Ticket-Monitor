import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from webdriver_handler import webDriverHanlder

class cuaMonitor:
    def __init__(self, web_driver) -> None:
        self.web_driver = web_driver
        self.web_driver_handler = webDriverHanlder(web_driver)
        self.login_url = "https://m.flycua.com/login"
        self.home_url = "https://m.flycua.com/index"

    # Enter the phone number to input slot
    def enterPhoneNum(self, wait_time) -> None:
        phone_number = input("Please Enter Phone Number: ")
        phone_num_slot_xpath = "//input[@placeholder='Mobile phone number']"
        success = False
        while not success:
            success = self.web_driver_handler.enter_content_to_element_by_xpath(phone_number, phone_num_slot_xpath, wait_time, element_id="Phone Number Slot")


    # Mark check on login agreements 
    def clickLoginAgrees(self, wait_time) -> None:
        login_agrees_xpath = "//div[@class='css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-6koalj r-18u37iz']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(login_agrees_xpath, wait_time, element_id="Login Agreement")


    # Ask user for picture verification code
    def enterPictureCode(self, wait_time) -> None:
        picture_verification_code = input("Please Enter Picture Verification Code: ")
        picture_verification_code_slot_xpath = "//input[@placeholder='Picture verification code']"
        success = False
        while not success:
            success = self.web_driver_handler.enter_content_to_element_by_xpath(picture_verification_code, picture_verification_code_slot_xpath, wait_time, element_id="Picture Verification Code Input Slot")


    # Click Send SMS code button
    def sendSmsCode(self, wait_time) -> None:
        get_code_xpath = "//div[@class='css-175oi2r r-lrvibr r-1awozwy r-1777fci r-qhyqy2 r-19gegkz r-atwnbb r-pcwgik r-dawwwy r-1phboty r-rs99b7 r-y47klf r-mabqd8 r-37tt59 r-19u6a5r r-7bouqp r-1loqt21 r-1otgn73']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(get_code_xpath, wait_time, element_id="Get SMS Code Button")
        print("\nSMS Verification Code Has Been Sent...")


    # Ask user for SMS verification code
    def enterSmsCode(self, wait_time) -> None:
        sms_verification_code = input("Please Enter SMS Verification Code：")
        sms_verification_code_input_slot_xpath = "//input[@placeholder='SMS verification code']"
        success = False
        while not success:
            success = self.web_driver_handler.enter_content_to_element_by_xpath(sms_verification_code, sms_verification_code_input_slot_xpath, wait_time, element_id="SMS Verification Code Input Slot")


    # Click login
    def clickLogin(self, wait_time) -> None:
        login_button_xpath = "//div[@class='css-175oi2r r-lrvibr r-1awozwy r-1777fci r-1m04atk r-1pyaxff r-1ag2gil r-pcwgik r-dawwwy r-1phboty r-rs99b7 r-y47klf r-eu3ka r-jv1ppg r-1loqt21 r-1otgn73']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(login_button_xpath, wait_time, element_id="Login Button")


    # Click Close Ad
    def clickCloseAd(self, wait_time) -> None:
        close_ad_xpath = "//div[@class='css-175oi2r r-1awozwy r-1niwhzg r-11mg6pl r-1q9bdsx r-rs99b7 r-6koalj r-1472mwg r-1777fci r-u8s1d r-1pgswnq r-1qd7xl r-lrsllp']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(close_ad_xpath, wait_time, element_id="Close Ad Button")


    def clickMy(self, wait_time) -> None:
        my_button_xpath = "//a[@href='/buyer/index']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(my_button_xpath, wait_time, element_id="MY")


    # Click 盲合
    def clickBlindBox(self, wait_time) -> None:
        blind_box_xpath = "//div/div/img[@src='https://cdn.flycua.com/_themes/main/dongtian/order-market.png']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(blind_box_xpath, wait_time, element_id="盲合")


    # Click 兑换
    def clickRedeem(self, wait_time) -> None:
        redeem_xpath = "//div[@class='css-1rynq56 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-1iln25a r-jwli3a r-191d75d r-1enofrn']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(redeem_xpath, wait_time, element_id="兑换", click_by_script=True)


    # Choose departure city
    def chooseDepartureCity(self, city, wait_time) -> None:
        choose_city_xpath = "//div[text()='选择出发城市']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(choose_city_xpath, wait_time, element_id="选择出发城市")

        target_city_xpath = f"//div[@style='flex-flow: row; justify-content: flex-start; align-items: center; height: 44px; padding-right: 12px; padding-left: 12px;']/div[text()='{city}']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(target_city_xpath, wait_time, element_id=f"{city}")


    # Choose arrival city
    def chooseArrivalCity(self, city, wait_time) -> None:
        choose_city_xpath = "//div[text()='选择到达城市']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(choose_city_xpath, wait_time, element_id="选择到达城市")

        target_city_xpath = f"//div[@style='flex-flow: row; justify-content: flex-start; align-items: center; height: 44px; padding-right: 12px; padding-left: 12px;']/div[text()='{city}']"
        success = False
        while not success:
            success = self.web_driver_handler.click_element_by_xpath(target_city_xpath, wait_time, element_id=f"{city}")


    def chooseDepartureTime(self, wait_time) -> bool:
        choose_date_xpath = "//div[text()='选择去程日期']"
        success = self.web_driver_handler.click_element_by_xpath(choose_date_xpath, wait_time, element_id="选择去程日期")
        if not success:
            return False

        date_xpath = "//div[@class='css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-1kihuf0 r-6koalj r-1777fci r-bnwqim r-pcwgik r-1xfd6ze r-uxrrfj r-2tyz2o r-jwli3a']/div[text()='出发']"
        return self.web_driver_handler.click_element_by_xpath(date_xpath, wait_time, element_id="日历-出发", click_by_script=True)


    def tryClickArrivalTime(self, wait_time) -> bool:
        choose_date_xpath = "//div[text()='选择返程日期']"
        success = self.web_driver_handler.click_element_by_xpath(choose_date_xpath, wait_time, element_id="选择返程日期")
        if not success:
            return False
        
        date_xpath = "//div[@class='css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-1kihuf0 r-6koalj r-1777fci r-bnwqim r-pcwgik r-1xfd6ze r-uxrrfj r-2tyz2o r-jwli3a']/div[text()='返程']"
        return self.web_driver_handler.click_element_by_xpath(date_xpath, wait_time, element_id="日历-返程")


    def isLogin(self) -> bool:
        login_status_text = "未登录"
        try:
            WebDriverWait(self.web_driver, 1).until( EC.presence_of_element_located((By.XPATH, f"//div[text()='{login_status_text}']")))
            return False
        except TimeoutException:
            return True

    def openCuaHomePage(self) -> None:
        self.web_driver.get(self.home_url)

    def openLoginPage(self) -> None:
        self.web_driver.get(self.login_url)

    def refreshPage(self) -> None:
        self.web_driver.refresh()

    # Bundle methods to login a user account on CUA website
    def loginAccount(self) -> None:
        self.openLoginPage()
        self.enterPhoneNum(20)
        self.clickLoginAgrees(5)
        self.enterPictureCode(5)
        self.sendSmsCode(5)
        self.enterSmsCode(5)
        self.clickLogin(5)

    def monitorTickets(self, departure_city, arrival_city, refresh_time_in_sec) -> None:
        self.clickMy(5)
        self.clickBlindBox(10)
        self.clickRedeem(5)

        success = False
        while not success:
            self.chooseDepartureCity(departure_city, 5)
            self.chooseArrivalCity(arrival_city, 5)
            if self.chooseDepartureTime(2):
                success = self.tryClickArrivalTime(2)
            else:
                success = False
                self.web_driver.refresh()
            time.sleep(refresh_time_in_sec)

        
    