from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FollowFollowers():
    def __init__(self, PATH, TARGET, USER, PASS):
        self.PATH = PATH
        self.TARGET = TARGET
        self.USER = USER
        self.PASS = PASS
        self.driver = webdriver.Chrome(executable_path=self.PATH)  # Creates driver
        self.login()
        self.find_followers()
        self.follow()

        
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[2]").click()
        sleep(0.5)  # Deals with COOKIES Popup

        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.USER)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.PASS)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(4)  # Logs User in via their Instagram User/Pass

        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
        # Deals with Notifications Popup

        
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{self.TARGET}/followers/")
        sleep(4)  # After Logging in, open the Target Accounts Followers list page

        for i in range(0, 4):  # Loads 4 more pages of 12 Accounts
            wheel = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", wheel)
            sleep(1)  # It scrolls the Follower Section 4 times (1 second wait for it to load new accounts)
        sleep(2)

        
    def follow(self):
        for i in range(1, 50):
            self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button').click()
            sleep(0.5)
            # Scrolling means that <li> now has 60 items intead of the initial 12
            # For loop lets us simply follow each one
            # Note Instagram doesn't let you follow that many people in a short time frame
