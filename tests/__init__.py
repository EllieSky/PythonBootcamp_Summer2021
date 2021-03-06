from configparser import ConfigParser

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_HOME = os.path.dirname(TEST_DIR)

BROWSER = os.environ.get('BROWSER') or "chrome"
TEST_ENV = os.environ.get('TEST_ENV') or "default"
HEADLESS = os.environ.get('HEADLESS') == "True"

config = ConfigParser()
config.read(f'{PROJ_HOME}/config.ini')

DOMAIN = config.get(TEST_ENV, 'DOMAIN')

BASE_URL = f"{DOMAIN}/symfony/web/index.php"

ADMIN_USER = config.get(TEST_ENV, 'ADMIN_USERNAME')
DEFAULT_PASSWORD = config.get(TEST_ENV, 'DEFAULT_ADMIN_PASSWORD')

DEFAULT_WAIT = config.get(TEST_ENV, 'DEFAULT_WAIT')


class DriverPath:

    @classmethod
    @property
    def FIREFOX(cls):
        if not os.environ.get('_firefox'):
            os.environ.setdefault('_firefox', GeckoDriverManager().install())
        return os.environ.get('_firefox')

    @classmethod
    @property
    def CHROME(cls):
        if not os.environ.get('_chrome'):
            os.environ.setdefault('_chrome', ChromeDriverManager().install())
        return os.environ.get('_chrome')
