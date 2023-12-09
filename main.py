from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

login_url = "https://m.flycua.com/login"
home_url = "https://m.flycua.com/index"
#phone_number = "13534367410"
phone_number = "13112756019"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(login_url)
#driver.get(home_url)

# Enter the phone number
phone_num_placeholder_value = "Mobile phone number"
try:
    phone_number_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{phone_num_placeholder_value}']")))
    phone_number_input.send_keys(phone_number)
except NoSuchElementException:
    print("ERROR: Phone Number Input Element Not Founded After Waiting...")
    exit()


# Click login agreements check
login_agrees_class_value = "css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-6koalj r-18u37iz"
try:
    login_agrees = driver.find_element(By.XPATH, f"//div[@class='{login_agrees_class_value}']")
    login_agrees.click()
except NoSuchElementException:
    print("ERROR: Login Agreement Check Button Not Founded")
    exit()

# Ask user for picture verification code
picture_verification_code = input("输入图片验证码: ")
picture_verification_code_placeholder_value = "Picture verification code"
try:
    picture_verification_code_input = driver.find_element(By.XPATH, f"//input[@placeholder='{picture_verification_code_placeholder_value}']")
    picture_verification_code_input.send_keys(picture_verification_code)
except NoSuchElementException:
    print("ERROR: Picture Verification Code Input Slot Not Founded")
    exit()

# Click get SMS code button
get_code_class_value = "css-175oi2r r-lrvibr r-1awozwy r-1777fci r-qhyqy2 r-19gegkz r-atwnbb r-pcwgik r-dawwwy r-1phboty r-rs99b7 r-y47klf r-mabqd8 r-37tt59 r-19u6a5r r-7bouqp r-1loqt21 r-1otgn73"
try:
    get_code = driver.find_element(By.XPATH, f"//div[@class='{get_code_class_value}']")
    get_code.click()
except NoSuchElementException:
    print("ERROR: Get SMS Code Button Not Founded")
    exit()

# Ask user for SMS verification code
print("\n短信验证码已发出...")
sms_verification_code = input("输入短信验证码：")
sms_verification_code_placeholder_value = "SMS verification code"
try:
    sms_verification_code_input = driver.find_element(By.XPATH, f"//input[@placeholder='{sms_verification_code_placeholder_value}']")
    sms_verification_code_input.send_keys(sms_verification_code)
except NoSuchElementException:
    print("ERROR: SMS Verification Code Input Slot Not Founded")
    exit()

# Click login
login_class_value = "css-175oi2r r-lrvibr r-1awozwy r-1777fci r-1m04atk r-1pyaxff r-1ag2gil r-pcwgik r-dawwwy r-1phboty r-rs99b7 r-y47klf r-eu3ka r-jv1ppg r-1loqt21 r-1otgn73"
try:
    login = driver.find_element(By.XPATH, f"//div[@class='{login_class_value}']")
    login.click()
except NoSuchElementException:
    print("ERROR: Login Button Not Founded")
    exit()

#time.sleep(5)

# Click Close Ad
close_ad_class_value = "css-175oi2r r-1awozwy r-1niwhzg r-11mg6pl r-1q9bdsx r-rs99b7 r-6koalj r-1472mwg r-1777fci r-u8s1d r-1pgswnq r-1qd7xl r-lrsllp"
try:
    close_ad = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{close_ad_class_value}']")))
    #close_ad = driver.find_element(By.XPATH, f"//div[@class='{close_ad_class_value}']")
    close_ad.click()
except NoSuchElementException:
    print("ERROR: Close Ad Button Not Founded")
    exit()

#time.sleep(1)

# Click My
my_href_value = "/buyer/index"
try:
    my = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, f"//a[@href='{my_href_value}']")))
    #my = driver.find_element(By.XPATH, f"//a[@href='{my_href_value}']")
    print(my.get_attribute("outerHTML"))
    print("\n")
    my.click()
except NoSuchElementException:
    print("ERROR: 'My' Button Not Founded")
    exit()

#time.sleep(1)

# Click 盲合
blind_box_icon_src = "https://cdn.flycua.com/_themes/main/dongtian/order-market.png"
try:
    blind_box = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, f"//div/div/img[@src='{blind_box_icon_src}']")))
    #blind_box = driver.find_element(By.XPATH, f"//div/div/img[@src='{blind_box_icon_src}']")
    print(blind_box.get_attribute("outerHTML"))
    print("\n")
    blind_box.click()
except NoSuchElementException:
    print("ERROR: 盲合 Button Not Founded")
    exit()

#time.sleep(1)

# Click 兑换
redeem_class_value = "css-1rynq56 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-1iln25a r-jwli3a r-191d75d r-1enofrn"
try:
    redeem = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, f"//div[@class='{redeem_class_value}']")))
    # redeem = driver.find_element(By.XPATH, f"//div[@class='{redeem_class_value}']")
    print(redeem.get_attribute("outerHTML"))
    print("\n")
    redeem.click()
except NoSuchElementException:
    print("ERROR: 兑换 Button Not Founded")
    exit()

#time.sleep(1)

# Choose departure city
departure_class_value = "css-1rynq56"
try:
    elemets = WebDriverWait(driver, 10).until( EC.presence_of_all_elements_located((By.XPATH, f"//div[@class='{departure_class_value}']")))
    #elemets = driver.find_elements(By.XPATH, f"//div[@class='{departure_class_value}']")
    for ele in elemets:
        print(ele.get_attribute("outerHTML"))
        print("\n")
    elemets[0].click()
except NoSuchElementException:
    print("ERROR: Elements Not Founded")
    exit()



