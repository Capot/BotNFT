from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

projetos = [
    'https://www.jpg.store/collection/theapesociety',
    'https://www.jpg.store/collection/cabins-theapesociety',
    # 'https://www.jpg.store/collection/havocworlds',
    #'https://www.jpg.store/collection/puurrtycatssociety',
    # 'https://www.jpg.store/collection/snowpunkz',
    # 'https://www.jpg.store/collection/pandasociety',
    # 'https://www.jpg.store/collection/smoothyetimountainclub',
    # 'https://www.jpg.store/collection/adaapeclub',
    # 'https://www.jpg.store/collection/discosolaris',
    'https://www.jpg.store/collection/chilledkongs',
    # 'https://www.jpg.store/collection/borgclub',
    # 'https://www.jpg.store/collection/jukeboys-generation1'
    # 'https://www.jpg.store/collection/mutantcrocs'
]
tempo = 15
tempo2 = 5


class NFTBot:


    def __init__(self):
        self.contador = 1
        self.bitcoinold = 0

        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        self.navegador = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)  # Backgroud
        # self.navegador = webdriver.Chrome(ChromeDriverManager().install())

    def VerificaFloor(self, projeto):
        self.projeto = projeto

        self.navegador.get(self.projeto)
        time.sleep(tempo)

        self.floor = self.navegador.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

        self.VerificaVendas()

    def VerificaVendas(self):
        self.navegador.get(self.projeto+'?tab=activity')
        time.sleep(tempo2)

        self.ultimaVendavalor = self.navegador.find_element_by_xpath(
            '//*[@id="app"]/div[2]/section/div/div[1]/table/tbody/tr[1]/td[4]/div/p').text
        self.ultimaVendatempo = self.navegador.find_element_by_xpath(
            '//*[@id="app"]/div[2]/section/div/div[1]/table/tbody/tr[1]/td[7]').text

        self.VerificaCotacao()

    def VerificaCotacao(self):
        time.sleep(tempo2)

        self.navegador.get('https://www.google.com/search?q=bitcoin+dolar&rlz=1C1ISCS_pt-PTBR975BR975&oq=bitcoin+dolar&aqs=chrome..69i57.4577j0j4&sourceid=chrome&ie=UTF-8')
        self.bitcoin = self.navegador.find_element_by_xpath(
            '//*[@id="crypto-updatable_2"]/div/div[2]/span[1]'
        ).text

        time.sleep(tempo2)
        self.navegador.get(
            'https://www.google.com/search?q=cardano+hoje&rlz=1C1ISCS_pt-PTBR975BR975&oq=carda&aqs=chrome.0.69i59j69i57.1282j0j9&sourceid=chrome&ie=UTF-8')
        self.cardano = self.navegador.find_element_by_xpath(
            '//*[@id="crypto-updatable_2"]/div/div[2]/span[1]'
        ).text

    def ImprimiFloor(self):
        print('BTC: {} USD                                             ADA: {} BRL' .format(self.bitcoin, self.cardano))
        print('|{:=^80}|'.format('Floor'))
        print('Projeto: {}' .format(self.projeto[33:]))
        print('Floor:', int(self.floor))
        print('')
        print('Ultima Venda: {}      Tempo: {}                    S: {}'.format(self.ultimaVendavalor, self.ultimaVendatempo,  self.contador))
        print('-' * 80)
        #print('contador:', self.contador)
        print('')

        self.contador = self.contador + 1

robo = NFTBot()

while True:
    for i in projetos:
        robo.VerificaFloor(i)
        robo.ImprimiFloor()


