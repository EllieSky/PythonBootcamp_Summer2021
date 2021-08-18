from webdriver_manager.chrome import ChromeDriverManager
import os

BROWSER = "chrome"
CHROME_PATH = ChromeDriverManager().install()

DOMAIN = "http://hrm-online.portnov.com/"

ADMIN_USER = "admin"
DEFAULT_PASSWORD = "password"

DEFAULT_WAIT = 7

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_HOME = os.path.dirname(TEST_DIR)
