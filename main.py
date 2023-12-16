from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from cua_monitor import cuaMonitor
from cookies_handler import cookiesHandler

# CUA Account phone number
#phone_number = "13534367410"
phone_number = "13112756019"
departure_city = "佛山"
arrival_city = "哈尔滨"

cookies_file_name = "cookies.pkl"

# Create Web Driver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Create CUA Monitor
monitor = cuaMonitor(driver)

# Create a Cookies Handler
cookies_handler = cookiesHandler(driver, cookies_file_name)

monitor.openCuaHomePage()

if cookies_handler.cookiesExist():
    cookies_handler.getCookies()
    monitor.refreshPage()

monitor.clickCloseAd(50)

# Check Login Status
if monitor.isLogin():
    monitor.monitorTickets(departure_city, arrival_city, 5)
else:  
    monitor.loginAccount(phone_number)
    monitor.clickCloseAd(50)
    cookies_handler.saveCookies()
    monitor.monitorTickets(departure_city, arrival_city, 5)

