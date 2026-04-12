from pathlib import Path
from playwright.sync_api import sync_playwright
import pandas as pd
import random
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    site = Path(__file__).parent / "produtos.html"
    page.goto(f"file:///{site}")
    tab = Path(__file__).parent / "produtos.csv"
    tabela = pd.read_csv(tab)

    for linha in tabela.index:
        time_random = random.uniform(0.3, 0.7)
        time.sleep(time_random)
        codigo = tabela.loc[linha, "codigo"]
        page.type("input[id=codigo]", str(codigo), delay=200)
        time_random = random.uniform(0.3, 0.7)
        time.sleep(time_random)
        marca = tabela.loc[linha, "marca"]
        page.type("input[id=marca]", str(marca), delay=100)
        time_random = random.uniform(0.3, 0.7)
        time.sleep(time_random)
        tipo = tabela.loc[linha, "tipo"]
        page.type("input[id=tipo]", str(tipo), delay=120)
        time_random = random.uniform(0.3, 0.7)
        time.sleep(time_random)
        categoria = tabela.loc[linha, "categoria"]
        page.type("input[id=categoria]", str(categoria), delay=120)
        time_random = random.uniform(0.3, 0.7)
        time.sleep(time_random)
        preco_unitario = tabela.loc[linha, "preco_unitario"]
        page.type("input[id=preco_unitario]", str(preco_unitario), delay=200)
        time_random = random.uniform(0.3, 0.7)
        time.sleep(time_random)
        custo = tabela.loc[linha, "custo"]
        page.type("input[id=custo]", str(custo), delay=200)
        time_random = random.uniform(0.3, 0.7)
        time.sleep(time_random)
        obs = tabela.loc[linha, "obs"]
        page.type("input[id=obs]", str(obs), delay=104)
        time_random = random.uniform(0.3, 0.7)
        time.sleep(1)
        page.click("button[type=submit]")