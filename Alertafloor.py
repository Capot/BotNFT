from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import PySimpleGUI as sg
import time

tempo = 8

class TeladeAlerta:

    def __init__(self, projeto, floor):
        #sg.theme('Reddit')
        # Layout
        self.projeto = projeto
        self.floor = floor
        layout = [
            [sg.Text('Alerta de Floor!')],
            [sg.Text(self.projeto[33:])],
            [sg.Text(self.floor)],

            [sg.Text('Projeto:', size=(10, 0)), sg.Input(self.projeto)],

            [sg.Button('OK', key='ok')],
        ]

        # Janela
        self.janela = sg.Window('ALERTA DE FLOOR', size=(480, 150)).layout(layout)

    def Iniciar(self):
        while True:
            # Ler Eventos
            self.eventos, self.valores = self.janela.read()

            if self.eventos == 'ok':
                break



class NFTBot:

    def __init__(self):

        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        self.navegador = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)  # Backgroud
        # self.navegador = webdriver.Chrome(ChromeDriverManager().install())



    def VerificaFloor(self, projeto, valor):
        self.projeto = projeto
        self.valor = valor

        self.navegador.get(self.projeto)
        time.sleep(tempo)

        self.floor = self.navegador.find_element_by_xpath('//*[@id="__next"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text
        self.Alerta()

    def Alerta(self):
        #print(self.projeto, int(self.floor))

        if int(self.floor) <= self.valor:
            print('Alerta!')
            abreAlerta = TeladeAlerta(self.projeto, int(self.floor))
            abreAlerta.Iniciar()
            #sg.popup('Alerta', self.projeto, title='Alerta de Floor')

        else:

            print('|{:=^80}|'.format('Floor'))
            print('Projeto:', self.projeto[33:])
            print('Valor:', int(self.floor))
            print('-' * 80)
            # print('contador:', self.contador)
            print('')
            #time.sleep(2)
            #self.navegador.refresh()

robo = NFTBot()

while True:

    robo.VerificaFloor('https://www.jpg.store/collection/chilledkongs', 400)
    robo.VerificaFloor('https://www.jpg.store/collection/borgclub', 300)
    robo.VerificaFloor('https://www.jpg.store/collection/zombiehunters', 55)
    robo.VerificaFloor('https://www.jpg.store/collection/bosscatrocketclub', 300)

