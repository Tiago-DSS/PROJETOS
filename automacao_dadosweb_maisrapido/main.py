from playwright.sync_api import sync_playwright
import time
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    page.fill("input[type=text]", "stuartlittle@gmail.com")
    page.fill("input[type=password]", "P@ssw0rd123")
    page.click("button[type=submit]")
    tabela = pd.read_csv("C:/projetos_programacao/vscode/projetos/automacao_dadosweb_maisrapido/produtos.csv")
    page.wait_for_selector("input[id=codigo]")
    for linha in tabela.index:
        codigo = tabela.loc[linha, "codigo"]
        page.fill("input[id=codigo]", str(codigo))
        marca = tabela.loc[linha, "marca"]
        page.fill("input[id=marca]", str(marca))
        tipo = tabela.loc[linha, "tipo"]
        page.fill("input[id=tipo]", str(tipo))
        categoria = tabela.loc[linha, "categoria"]
        page.fill("input[id=categoria]", str(categoria))
        preco_unitario = tabela.loc[linha, "preco_unitario"]
        page.fill("input[id=preco_unitario]", str(preco_unitario))
        custo = tabela.loc[linha, "custo"]
        page.fill("input[id=custo]", str(custo))
        obs = tabela.loc[linha, "obs"]
        page.fill("input[id=obs]", str(obs))
        page.click("button[type=submit]")
    time.sleep(60) #só para ver o resultado antes de fechar o navegador


