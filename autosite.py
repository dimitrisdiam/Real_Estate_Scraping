
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CHROME_DRIVER_PATH = '/Users/USER/Documents/Development/chromedriver'


class ZillowScraper:

    def bring_the_data(self, zillow_pagelink):

        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get(zillow_pagelink)

        # Automation.
        self.driver.maximize_window()
        for _ in range(20):
            webdriver.ActionChains(self.driver).key_down(Keys.TAB).perform()
        for _ in range(120):
            webdriver.ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        print(soup.prettify())


        houses_links = soup.find_all("a", class_="list-card-link", href=True, tabindex="-1")
        houses_prices = soup.find_all("div", class_="list-card-price")
        houses_addresses = soup.find_all("address", class_="list-card-addr")

        self.links = [link["href"] for link in houses_links]
        self.prices = [price.text.split("+")[0].split("/mo")[0] for price in houses_prices]
        self.addresses = [address.text for address in houses_addresses]


    def complete_the_doc(self, form):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get(form)

        for address in range(len(self.addresses)):

            address_input = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            address_input.send_keys(self.addresses[address-1])

            price_input = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            price_input.send_keys(self.prices[address-1])

            link_input = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            if self.links[address-1][0] == "/":
                link_input.send_keys('https://www.zillow.com'+self.links[address - 1])
            else:
                link_input.send_keys(self.links[address-1])

            # Submit Button.
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div'))).click()

            # New Answer.
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))).click()
