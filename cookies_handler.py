import pickle
import os

class cookiesHandler:
    def __init__(self, web_driver, file_name) -> None:
        self.web_driver = web_driver
        self.cookies_file_name = file_name
        
        
    def getCookies(self) -> None:
        with open(self.cookies_file_name, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                self.web_driver.add_cookie(cookie)


    def saveCookies(self) -> None:
        cookies = self.web_driver.get_cookies()
        with open(self.cookies_file_name, "wb") as file:
            pickle.dump(cookies, file)

    def cookiesExist(self) -> bool:
        return os.path.exists(self.cookies_file_name) and os.path.getsize(self.cookies_file_name) > 0