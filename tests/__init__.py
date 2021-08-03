import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



BROWSER = "chrome"
CHROME_PATH = ChromeDriverManager().install()

DOMAIN = "http://hrm-online.portnov.com/"

ADMIN_USER = "admin"
DEFAULT_PASSWORD = "password"


