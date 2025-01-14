import pyautogui
import time
import pandas

pyautogui.PAUSE=0.5

#passo 1-abrir o sistema
 #   sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")    
pyautogui.press("enter")
pyautogui.click(x=447, y=909)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#passo 2- Fazer login
pyautogui.click(x=811, y=466)
pyautogui.write("teste@teste.com")
pyautogui.click(x=762, y=589)
pyautogui.write("senha")
pyautogui.click(x=953, y=671)
#passo 3- Importar base de produtos

tabela = pandas.read_csv("produtos.csv")
print (tabela)
time.sleep(2)

#passo 4- Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=584, y=320)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"]) 
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    #apertar botao para enviar produto
    pyautogui.press("enter")
    pyautogui.scroll(10000)



#passo 5-Repetir o 4 passo até acabar os produtos


