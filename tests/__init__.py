from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os

BROWSER = os.environ.get('BROWSER') or "chrome"

DOMAIN = "http://hrm-online.portnov.com"
BASE_URL = f"{DOMAIN}/symfony/web/index.php"

ADMIN_USER = "admin"
DEFAULT_PASSWORD = "password"

DEFAULT_WAIT = 7

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_HOME = os.path.dirname(TEST_DIR)


class DriverPath:
    @property
    def FIREFOX(self):
        return GeckoDriverManager().install()

    @property
    def CHROME(self):
        return ChromeDriverManager().install()
