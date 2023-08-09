import pytest
import ast

from pageObject.login import Login
from pageObject.openBrowser import OpenBrowser
from utilites.datareader import Data


class Test_001_login:
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['user_data'])

    @pytest.mark.order(1)
    def test_login(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        open_url.open_webBrowser()
        login.user_login(self.log)


