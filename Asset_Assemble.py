#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
import time


from selenium.webdriver.common.action_chains import ActionChains

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main(browser):

    browser.get('http://eip.chinatowercom.cn')
    time.sleep(2)

    # 登录
    browser.find_element_by_name("username").send_keys(u"zhaocan")
    browser.find_element_by_name("password").send_keys(u"yu56789")

    browser.find_element_by_xpath("//*[@id=\"fm1\"]/div[4]/button[1]").click()

    # 4a窗口的句柄
    handle_4a = browser.current_window_handle

    # 进入商合平台
    browser.find_element_by_xpath(
        "//*[@id=\"p_p_id_appcoll2_WAR_towerportlet_\"]/div/div/div/div/ul/li[11]/a[2]").click()

    # 处理新打开的窗口
    handles = browser.window_handles



if __name__ == '__main__':

    browser_Firefox = webdriver.Firefox()
    main(browser_Firefox)