import configparser
import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def config():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _file = os.path.abspath(cur_dir) + "\\" + "configurations\\config.ini"
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope='function')
def locator():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _file = os.path.abspath(cur_dir) + "\\" + "locators.ini"
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope='function')
def driver(request):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _chromedriver = os.path.abspath(cur_dir) + "\\" + "driver\\chromedriver.exe"
    s = Service(_chromedriver)
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver

    def fin():
        driver.close()

    request.addfinalizer(fin)
    return
