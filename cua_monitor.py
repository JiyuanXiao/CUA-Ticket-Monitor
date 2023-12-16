import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

class cuaMonitor:
    def __init__(self, web_driver) -> None:
        self.web_driver = web_driver
        self.login_url = "https://m.flycua.com/login"
        self.home_url = "https://m.flycua.com/index"

    # Enter the phone number to input slot
    def enterPhoneNum(self, phone_number, wait_time) -> None:
        phone_num_placeholder_value = "Mobile phone number"
        try:
            phone_number_input = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{phone_num_placeholder_value}']")))
            phone_number_input.send_keys(phone_number)
        except TimeoutException:
            print("ERROR: Phone Number Input Element Not Found After Waiting...")
            exit()

    # Mark check on login agreements 
    def clickLoginAgrees(self, wait_time) -> None:
        login_agrees_class_value = "css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-6koalj r-18u37iz"
        try:
            login_agrees = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{login_agrees_class_value}']")))
            login_agrees.click()
        except TimeoutException:
            print("ERROR: Login Agreement Check Button Not Found")
            exit()

    # Ask user for picture verification code
    def enterPictureCode(self, wait_time) -> None:
        picture_verification_code = input("输入图片验证码: ")
        picture_verification_code_placeholder_value = "Picture verification code"
        try:
            picture_verification_code_input = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{picture_verification_code_placeholder_value}']")))
            picture_verification_code_input.send_keys(picture_verification_code)
        except TimeoutException:
            print("ERROR: Picture Verification Code Input Slot Not Found")
            exit()

    # Click Send SMS code button
    def sendSmsCode(self, wait_time) -> None:
        get_code_class_value = "css-175oi2r r-lrvibr r-1awozwy r-1777fci r-qhyqy2 r-19gegkz r-atwnbb r-pcwgik r-dawwwy r-1phboty r-rs99b7 r-y47klf r-mabqd8 r-37tt59 r-19u6a5r r-7bouqp r-1loqt21 r-1otgn73"
        try:
            get_code = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{get_code_class_value}']")))
            get_code.click()
            print("\n短信验证码已发出...")
        except TimeoutException:
            print("ERROR: Get SMS Code Button Not Found")
            exit()

    # Ask user for SMS verification code
    def enterSmsCode(self, wait_time) -> None:
        sms_verification_code = input("输入短信验证码：")
        sms_verification_code_placeholder_value = "SMS verification code"
        try:
            sms_verification_code_input = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{sms_verification_code_placeholder_value}']")))
            sms_verification_code_input.send_keys(sms_verification_code)
        except TimeoutException:
            print("ERROR: SMS Verification Code Input Slot Not Found")
            exit()

    # Click login
    def clickLogin(self, wait_time) -> None:
        login_class_value = "css-175oi2r r-lrvibr r-1awozwy r-1777fci r-1m04atk r-1pyaxff r-1ag2gil r-pcwgik r-dawwwy r-1phboty r-rs99b7 r-y47klf r-eu3ka r-jv1ppg r-1loqt21 r-1otgn73"
        try:
            login = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{login_class_value}']")))
            login.click()
        except TimeoutException:
            print("ERROR: Login Button Not Found")
            exit()

    # Click Close Ad
    def clickCloseAd(self, wait_time) -> None:
        close_ad_class_value = "css-175oi2r r-1awozwy r-1niwhzg r-11mg6pl r-1q9bdsx r-rs99b7 r-6koalj r-1472mwg r-1777fci r-u8s1d r-1pgswnq r-1qd7xl r-lrsllp"
        try:
            close_ad = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{close_ad_class_value}']")))
            close_ad.click()
        except TimeoutException:
            print("ERROR: Close Ad Button Not Found")
            exit()

    def clickMy(self, wait_time) -> None:
        my_href_value = "/buyer/index"
        try:
            my = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//a[@href='{my_href_value}']")))
            my.click()
        except TimeoutException:
            print("ERROR: 'My' Button Not Found")
            exit()

    # Click 盲合
    def clickBlindBox(self, wait_time) -> None:
        blind_box_icon_src = "https://cdn.flycua.com/_themes/main/dongtian/order-market.png"
        try:
            blind_box = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div/div/img[@src='{blind_box_icon_src}']")))
            blind_box.click()
        except TimeoutException:
            print("ERROR: 盲合 Button Not Found")
            exit()

    # Click 兑换
    def clickRedeem(self, wait_time) -> None:
        redeem_class_value = "css-1rynq56 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-1iln25a r-jwli3a r-191d75d r-1enofrn"
        try:
            redeem = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{redeem_class_value}']")))
            #action = ActionChains(self.web_driver)
            #action.move_to_element_with_offset(redeem, -20, 0).click().perform()
            self.web_driver.execute_script("arguments[0].click();", redeem)
        except TimeoutException:
            print("ERROR: 兑换 Button Not Found")
            exit()

    # Choose departure city
    def chooseDepartureCity(self, city, wait_time) -> None:
        city_style_value = "flex-flow: row; justify-content: flex-start; align-items: center; height: 44px; padding-right: 12px; padding-left: 12px;"
        try:
            departure = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, "//div[text()='选择出发城市']")))
            departure.click()
        except TimeoutException:
            print("ERROR:  选择出发城市 Not Found")
            exit()

        try:
            departure_city = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@style='{city_style_value}']/div[text()='{city}']")))
            departure_city.click()
        except TimeoutException:
            print(f"ERROR:  {city} Not Found")
            exit()

    # Choose arrival city
    def chooseArrivalCity(self, city, wait_time) -> None:
        city_style_value = "flex-flow: row; justify-content: flex-start; align-items: center; height: 44px; padding-right: 12px; padding-left: 12px;"
        try:
            arrival = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, "//div[text()='选择到达城市']")))
            arrival.click()
        except TimeoutException:
            print("ERROR:  选择到达城市 Not Found")
            exit()

        try:
            arrival_city = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@style='{city_style_value}']/div[text()='{city}']")))
            arrival_city.click()
        except TimeoutException:
            print(f"ERROR:  {city} Not Found")
            exit()

    def chooseDepartureTime(self, wait_time) -> bool:
        try:
            departure = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, "//div[text()='选择去程日期']")))
            departure.click()
        except TimeoutException:
            print("ERROR:  选择去程日期 Not Found")
            return False
        except ElementClickInterceptedException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: ElementClickInterceptedException at 选择去程日期")
            return False

        class_value = "css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-1kihuf0 r-6koalj r-1777fci r-bnwqim r-pcwgik r-1xfd6ze r-uxrrfj r-2tyz2o r-jwli3a"
        try:
            departure_time = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{class_value}']/div[text()='出发']")))
            #action = ActionChains(self.web_driver)
            #action.move_to_element_with_offset(departure_time, 0, -20).click().perform()
            #departure_time.click()
            self.web_driver.execute_script("arguments[0].click();", departure_time)
            return True
        except TimeoutException:
            print("ERROR:  出发 Not Found")
            return False
        except ElementClickInterceptedException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: ElementClickInterceptedException at 日历-出发")
            return False

    def clickBack(self, wait_time) -> None:
        back_class_value = "css-175oi2r r-6koalj r-eqz5dr r-eu3ka r-1777fci r-1aockid"
        try:
            back = WebDriverWait(self.web_driver, wait_time).until(EC.presence_of_element_located((By.XPATH, f"//div[@class='{back_class_value}']")))
            print(back.get_attribute("outerHTML"))
            self.web_driver.execute_script("arguments[0].click();", back)
        except TimeoutException:
            print("ERROR: back Not Found")
            exit()

    def tryClickArrivalTime(self,departure_city, arrival_city, wait_time) -> bool:
        try:
            departure = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, "//div[text()='选择返程日期']")))
            departure.click()
        except TimeoutException:
            print("ERROR:  选择返程日期 Not Found")
            exit()

        class_value = "css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-1kihuf0 r-6koalj r-1777fci r-bnwqim r-pcwgik r-1xfd6ze r-uxrrfj r-2tyz2o r-jwli3a"
        try:
            departure_time = self.web_driver.find_element(By.XPATH, f"//div[@class='{class_value}']/div[text()='返程']")
            departure_time.click()
            return True
        except ElementClickInterceptedException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: ElementClickInterceptedException at 日历-返程")
            self.web_driver.refresh()
            return False
        except NoSuchElementException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {departure_city}-{arrival_city} Arrival Trip is Sold Out")
            self.web_driver.refresh()
            return False

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
    def loginAccount(self, account_phone_number) -> None:
        self.openLoginPage()
        self.enterPhoneNum(account_phone_number, 20)
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
            if self.chooseDepartureTime(5):
                success = self.tryClickArrivalTime(departure_city, arrival_city, 5)
                
            else:
                success = False
                self.web_driver.refresh()
            time.sleep(refresh_time_in_sec)

        
    