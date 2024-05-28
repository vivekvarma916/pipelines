import time
import pywinauto
import subprocess

class Flipkart():
    def __init__(self):

        self.appliances_section = '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/a[3]/div/div/span/span'
        self.washing_machine_section = '//*[@id="container"]/div/div[3]/div[4]/div/div[1]/a/div/div/img[2]'
        self.newfirst = '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[3]/div[4]'
        self.flights ='//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/a[4]/div/div'
        self.fromplaces = '//*[@id="container"]/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/div[1]/div[1]/input'
        self.toplaces = '//*[@id="container"]/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/div[1]/div[3]/div[1]/div[1]/input'
        self.depart_on = '//*[@id="container"]/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div/input'
        self.depart_date = '//*[@id="container"]/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div/table[1]/tbody/tr[3]/td[7]/div/button'
        self.search_button = '//*[@id="container"]/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/button'

    def desktop_functions(self, path):
        window_ref = pywinauto.application.Application().start(path)
        return window_ref