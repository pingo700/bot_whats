from selenium import webdriver
import time
dash_board='<div tabindex="-1" class="_2A8P4">'
button='<span data-testid="send" data-icon="send" class="">'
class controle:
    destinatario=''
    mensagem=''
    def __init__(self):
        print("Inicializando.",".",".")
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.ChromeOptions(executable_path=r'./chromedriver.exe')
    def enviar(self):
        #Adiciona o destinatário da mensagem 
        destinatario=input(string("Digite o nome do contato:"))
        #Adiciona a mensagem que será enviada
        mensagem=input(string("Digite o conteúdo da mensagem:"))
        #Localiza o Destinatario no navegador
        local=self.driver.find_element_by_xpath("//span[@title='{destinatario}']")
        #Clica no local
        local.click()
        time.sleep(2)
        #Localiza a barra de texto 
        chat=self.driver.find_element_by_class_name('_2A8P4')
        #Clica no chat
        chat.click()
        time.sleep(3)
        #Escreve a mensagem na barra de tarefas
        chat.send_keys(self.mensagem)
        #Procura o botão enviar
        enviar=self.driver.find_element_by_xpath("//span[@data-icon='send']")
        #Envia
        enviar.click()
        time.sleep(3)