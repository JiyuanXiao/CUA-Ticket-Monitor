from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from monitor_action import enter_phone_num, get_picture_code, get_sms_code, send_sms_code, click_login_agrees, click_login, click_close_ad, click_my, click_redeem, click_blind_box, choose_cities


# Setup Config Info
login_url = "https://m.flycua.com/login"
home_url = "https://m.flycua.com/index"
#phone_number = "13534367410"
phone_number = "13112756019"

# Setup Web Driver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Get Home Page
driver.get(home_url)

click_close_ad(driver, 50)

# Check Login Status
login_status_text = "未登录"
try:
    login_status =  WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, f"//div[text()='{login_status_text}']")))
except TimeoutException:
    click_my(driver, 5)
    click_blind_box(driver, 10)
    click_redeem(driver, 10)
    choose_cities(driver, 10)
    exit()

driver.get(login_url)

enter_phone_num(driver, phone_number, 20)
click_login_agrees(driver, 5)
get_picture_code(driver, 5)
send_sms_code(driver, 5)
get_sms_code(driver, 5)
click_login(driver, 5)
click_close_ad(driver, 50)
click_my(driver, 5)
click_blind_box(driver, 10)
click_redeem(driver, 10)
choose_cities(driver, 10)

