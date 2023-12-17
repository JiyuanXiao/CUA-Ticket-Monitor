from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By


class webDriverHanlder:
    def __init__(self, web_driver) -> None:
        self.web_driver = web_driver

    def click_element_by_xpath(self, xpath, wait_time, element_id, click_by_script=False) -> bool:
        try:
            element = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"{xpath}")))
            if click_by_script:
                self.web_driver.execute_script("arguments[0].click();", element)
            else:
                element.click()
            return True
        except ElementClickInterceptedException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: ElementClickInterceptedException at {element_id}")
            self.web_driver.refresh()
            return False
        except TimeoutException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: TimeoutException at {element_id}")
            self.web_driver.refresh()
            return False
        except NoSuchElementException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: NoSuchElementException at {element_id}")
            exit()
        
    def enter_content_to_element_by_xpath(self, content, xpath, wait_time, element_id) -> bool:
        try:
            element = WebDriverWait(self.web_driver, wait_time).until( EC.presence_of_element_located((By.XPATH, f"{xpath}")))
            element.send_keys(content)
            return True
        except TimeoutException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: TimeoutException at {element_id}")
            self.web_driver.refresh()
            return False
        except NoSuchElementException:
            print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: NoSuchElementException at {element_id}")
            exit()

    