##Buscando a tabela no YAhoo

!pip install yfinance # instala a biblioteca

import yfinance # importa uma biblioteca 

codigo = imput("Digite o código da ação desejada: ")
dados = yfinance.tricker(codigo).history("6mo") # abre uma tabela
fechamento = dados.close # escolhe na tabela qual a célula escolhida
fechamento.plot() # gráfico

##Análises solicitadas

maxima = fechamento.max()# Me da o valor máximo da tabela
minima = fechamento.min()# valor mínimo
atual  = fechamento.iloc[-1]# último valor da tabela

##Mandar um gmail automatizado

!pip install pyautogui## instalar biblioteca
!pip install pyperclip## instalar biblioteca

import pyautogui## importa a bibli (simulação de teclado e mouse)
import pyperclip## importa a bibli

pyautogui.PAUSE = 2# espera 2 segundos para rodar (menos erro)

pyautogui.hotkey("crtr","t")# abre uma aba na guia
pyperclip.copy("www.gmail.com")# armazena o texto
pyautogui.hotkey("ctrl","v")#cola o texto
pyautogui.hotkey("enter")# confirna e abre o gmail

#import time---time.sleep(5) vai atrasar 5 segundos para rodar o codigo
#pyautogui.position() <-- usar isso para saber a coordenada do mouse x=2019 y= 232

pyautogui.click(x=2019, y=232)# clica no escrever no gmail 
pyperclip.copy("XXX@gmail.com")
pyautogui.hotkey("crtl","v")
pyautogui.hotkey("enter")

pyperclip.copy("Análise Diária")
pyautogui.hotkey("crtl","v")
pyautogui.hotkey("enter")

mensagem = f""""
Prezado XXX,

segue as análises dos últimos seis meses da ação {codigo} conforme solicitado:

cotação máxima: R${round(maxima, 2)}
cotação minima: R${round(minima, 2)}
cotação atual : R${round(atual), 2}

Qualquer dúvida estou a disposição!

Atte.
"""
pyperclip.copy(mensagem)
pyautogui.hotkey("crtl","v")
pyautogui.hotkey("enter")

pyautogui.click(x=3090, y=1031)

#time importe x=3069 y=1031









 




