from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import flipkart_obj
import unittest
from object import flipkart
import time

# # Set the path to your ChromeDriver executable
# chrome_driver_path = "C:\Program Files\Python38\chromedriver.exe"
#
# # Initialize the Chrome browser
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.maximize_window()
#
# # Open the Flipkart website
# driver.get("https://www.flipkart.com")
#
# # Search for laptops
# search_box = driver.find_element(By.XPATH, "//input[@title='Search for Products, Brands and More']")
# search_box.send_keys("laptops")
# search_box.send_keys(Keys.ENTER)
#
# # Wait for HP laptops to appear
# #wait = WebDriverWait(driver, 40)
# #wait.until(EC.presence_of_element_located((By.XPATH, "//div[@title='HP']//div[@class='_1p7h2j']")))
#
# # Click on HP laptops
# #driver.find_element(By.XPATH, "//div[@title='HP']//div[@class='_1p7h2j']").click()
#
# # Now you can extract information about i7 processors or perform any other actions you need
#
# # Close the browser
# driver.quit()
class flipkart_tests(unittest.TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_01_flipkart_pageopen(self):
        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        # Open the Flipkart website
        self.driver.get("https://www.flipkart.com")

        # Search for laptops
        search_box = self.driver.find_element(By.XPATH, "//input[@title='Search for Products, Brands and More']")
        search_box.send_keys("laptops")
        search_box.send_keys(Keys.ENTER)

        # Wait for HP laptops to appear
        # wait = WebDriverWait(driver, 40)
        # wait.until(EC.presence_of_element_located((By.XPATH, "//div[@title='HP']//div[@class='_1p7h2j']")))

        # Click on HP laptops
        # driver.find_element(By.XPATH, "//div[@title='HP']//div[@class='_1p7h2j']").click()

        # Now you can extract information about i7 processors or perform any other actions you need

        # Close the browser
        self.driver.quit()

    def test_02_flipkart_click_flights_section(self):

        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        # Open the Flipkart website
        self.driver.get("https://www.flipkart.com")

        # search for appliances location
        time.sleep(10)
        self.driver.find_element(By.XPATH, flipkart.flights).click()
        time.sleep(2)

        self.driver.quit()

    def test_03_flipkart_search_flights(self):

        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        # Open the Flipkart website
        self.driver.get("https://www.flipkart.com")

        # search for appliances location
        self.driver.find_element(By.XPATH, flipkart.flights).click()
        time.sleep(10)

        #select washing machine section
        from_place = "Mumbai, BOM - Chatrapati Shivaji International Airport"
        to_place = "Chennai, MAA - Chennai International Airport"
        self.driver.find_element(By.XPATH, flipkart.fromplaces).send_keys(from_place)

        time.sleep(2)
        self.driver.find_element(By.XPATH, flipkart.toplaces).send_keys(to_place)
        time.sleep(2)
        # self.driver.find_element(By.XPATH, flipkart.depart_on).click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH, flipkart.depart_date).click()
        # time.sleep(1)
        self.driver.find_element(By.XPATH, flipkart.search_button).click()
        time.sleep(6)
        self.driver.quit()

    # def test_04_flipkart_select_newfirst_option(self):
    #     chrome_driver_path = "C:\Program Files\Python38\chromedriver.exe"
    #
    #     # Initialize the Chrome browser
    #     self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
    #     self.driver.maximize_window()
    #
    #     # Open the Flipkart website
    #     self.driver.get("https://www.flipkart.com")
    #
    #     # search for appliances location
    #     self.driver.find_element(By.XPATH, flipkart.appliances_section).click()
    #     time.sleep(5)
    #
    #     # select washing machine section
    #     self.driver.find_element(By.XPATH, flipkart.washing_machine_section).click()
    #     time.sleep(4)
    #
    #     #select newfirst option in the page
    #     self.driver.find_element(By.XPATH, flipkart.newfirst).click()
    #     time.sleep(4)
    #
    #     self.driver.quit()
