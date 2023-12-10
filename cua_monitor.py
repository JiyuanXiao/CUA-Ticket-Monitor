from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
            print("ERROR: Phone Number Input Element Not Founded After Waiting...")
            exit()

    # Mark check on login agreements 
    def clickLoginAgrees(self, wait_time) -> None:
        login_agrees_class_value = "css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-6koalj r-18u37iz"
        try:
            login_agrees = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{login_agrees_class_value}']")))
            login_agrees.click()
        except TimeoutException:
            print("ERROR: Login Agreement Check Button Not Founded")
            exit()

    # Ask user for picture verification code
    def enterPictureCode(self, wait_time) -> None:
        picture_verification_code = input("输入图片验证码: ")
        picture_verification_code_placeholder_value = "Picture verification code"
        try:
            picture_verification_code_input = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{picture_verification_code_placeholder_value}']")))
            picture_verification_code_input.send_keys(picture_verification_code)
        except TimeoutException:
            print("ERROR: Picture Verification Code Input Slot Not Founded")
            exit()

    # Click Send SMS code button
    def sendSmsCode(self, wait_time) -> None:
        get_code_class_value = "css-175oi2r r-lrvibr r-1awozwy r-1777fci r-qhyqy2 r-19gegkz r-atwnbb r-pcwgik r-dawwwy r-1phboty r-rs99b7 r-y47klf r-mabqd8 r-37tt59 r-19u6a5r r-7bouqp r-1loqt21 r-1otgn73"
        try:
            get_code = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{get_code_class_value}']")))
            get_code.click()
            print("\n短信验证码已发出...")
        except TimeoutException:
            print("ERROR: Get SMS Code Button Not Founded")
            exit()

    # Ask user for SMS verification code
    def enterSmsCode(self, wait_time) -> None:
        sms_verification_code = input("输入短信验证码：")
        sms_verification_code_placeholder_value = "SMS verification code"
        try:
            sms_verification_code_input = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{sms_verification_code_placeholder_value}']")))
            sms_verification_code_input.send_keys(sms_verification_code)
        except TimeoutException:
            print("ERROR: SMS Verification Code Input Slot Not Founded")
            exit()

    # Click login
    def clickLogin(self, wait_time) -> None:
        login_class_value = "css-175oi2r r-lrvibr r-1awozwy r-1777fci r-1m04atk r-1pyaxff r-1ag2gil r-pcwgik r-dawwwy r-1phboty r-rs99b7 r-y47klf r-eu3ka r-jv1ppg r-1loqt21 r-1otgn73"
        try:
            login = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{login_class_value}']")))
            login.click()
        except TimeoutException:
            print("ERROR: Login Button Not Founded")
            exit()

    # Click Close Ad
    def clickCloseAd(self, wait_time) -> None:
        close_ad_class_value = "css-175oi2r r-1awozwy r-1niwhzg r-11mg6pl r-1q9bdsx r-rs99b7 r-6koalj r-1472mwg r-1777fci r-u8s1d r-1pgswnq r-1qd7xl r-lrsllp"
        try:
            close_ad = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{close_ad_class_value}']")))
            close_ad.click()
        except TimeoutException:
            print("ERROR: Close Ad Button Not Founded")
            exit()

    def clickMy(self, wait_time) -> None:
        my_href_value = "/buyer/index"
        try:
            my = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//a[@href='{my_href_value}']")))
            my.click()
        except TimeoutException:
            print("ERROR: 'My' Button Not Founded")
            exit()

    # Click 盲合
    def clickBlindBox(self, wait_time) -> None:
        blind_box_icon_src = "https://cdn.flycua.com/_themes/main/dongtian/order-market.png"
        try:
            blind_box = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div/div/img[@src='{blind_box_icon_src}']")))
            blind_box.click()
        except TimeoutException:
            print("ERROR: 盲合 Button Not Founded")
            exit()

    # Click 兑换
    def clickRedeem(self, wait_time) -> None:
        redeem_class_value = "css-1rynq56 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-1iln25a r-jwli3a r-191d75d r-1enofrn"
        try:
            redeem = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{redeem_class_value}']")))
            print(redeem.get_attribute("outerHTML"))
            print("\n")
            redeem.click()
        except TimeoutException:
            print("ERROR: 兑换 Button Not Founded")
            exit()

    # Choose departure city
    def chooseCities(self, wait_time) -> None:
        departure_class_value = "css-1rynq56"
        try:
            elemets = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_all_elements_located((By.XPATH, f"//div[@class='{departure_class_value}']")))
            for ele in elemets:
                print(ele.get_attribute("outerHTML"))
                print("\n")
            elemets[0].click()
        except TimeoutException:
            print("ERROR: Elements Not Founded")
            exit()

    def isLogin(self) -> bool:
        login_status_text = "未登录"
        try:
            WebDriverWait(self.web_driver, 5).until( EC.presence_of_element_located((By.XPATH, f"//div[text()='{login_status_text}']")))
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

    def monitorTickets(self) -> None:
        self.clickMy(5)
        self.clickBlindBox(10)
        self.clickRedeem(10)
        self.chooseCities(10)
    