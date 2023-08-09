class OpenBrowser:

    def __init__(self, driver, config):
        self.driver = driver
        self.webLink = config["common info"]["baseURL"]

    def open_webBrowser(self):
        baseURL = self.webLink
        self.driver.get(baseURL)
        self.driver.implicitly_wait(20)
