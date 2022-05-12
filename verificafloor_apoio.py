from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import PySimpleGUI as sg
import time

projetos = [
    'https://www.jpg.store/collection/theadapessociety',
    'https://www.jpg.store/collection/adaapeclub-season2',
    'https://www.jpg.store/collection/adaapeclub'
]
tempo = 15


class NFTBot:

    def __init__(self):
        self.contador = 1

        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        self.navegador = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)  # Backgroud
        #self.navegador = webdriver.Chrome(ChromeDriverManager().install())

    def VerificaFloor(self, projeto):
        self.projeto = projeto
        self.navegador.get(self.projeto)
        time.sleep(tempo)

        self.floor = self.navegador.find_element_by_xpath(
            '//*[@id="__next"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

        # while True:
        self.ImprimiFloor()

    def ImprimiFloor(self):
        print('|{:=^80}|'.format('Floor'))
        print('Projeto:', self.projeto[33:])
        print('Valor:', int(self.floor))
        print('-' * 80)
        #print('contador:', self.contador)
        print('')

        self.contador = self.contador + 1

robo = NFTBot()

while True:
    robo.VerificaFloor('https://www.jpg.store/collection/theadapessociety')
    robo.VerificaFloor('https://www.jpg.store/collection/adaapeclub')
    robo.VerificaFloor('https://www.jpg.store/collection/adaapeclub-season2')

