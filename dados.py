from pathlib import Path
import pandas as pd
import csv

ARQUIVO = Path("dados/dados_brutos.csv")
COLS = ["Titulo", "Rua", "Metros", "Quartos",
        "Banheiro", "Garagem", "Preço","Link"]

def criar_arquivo_csv():
    """Cria o CSV com cabeçalho"""
    pd.DataFrame(columns=COLS).to_csv(
        ARQUIVO,
        index=False,
        sep=';'
    )

def adicionar_dados_brutos(titulo, rua, metros,
                           quartos, banheiros, garagem, preco, link):
    '''Adiciona um linha ao final do arquivo csv'''
    nova_linha = pd.DataFrame([{
        "Titulo": titulo,
        "Rua": rua,
        "Metros": metros,
        "Quartos": quartos,
        "Banheiro": banheiros,
        "Garagem": garagem,
        "Preço": preco,
        "Link": link,
        "Id": link.replace('/?source=ranking%2Crp','').split('-id-')[-1]
    }])
    header = not ARQUIVO.exists() or ARQUIVO.stat().st_size == 0
    nova_linha.to_csv(
        ARQUIVO,
        mode='a',
        header=header,
        index=False,
        sep=';',
        quoting=csv.QUOTE_MINIMAL
    )

def tirar_duplicados():
    '''Tratamento de dados para tirar os dados duplicados'''
    df = pd.read_csv('dados/dados_brutos.csv', sep=';')
    cols_para_juntar = ['Titulo', 'Rua', 'Metros','Quartos','Banheiro','Preço']
    df['Concatenados'] = (
        df[cols_para_juntar]
        .astype(str)
        .agg(''.join, axis=1)
    )
    idx = df[
        (df['Titulo'] != "Setor Marista, Goiânia") |
        (df['Id'] == "Tem mais de um anuncio nesse imovel")
        ].index
    df.drop(idx, inplace=True)
    df = df.drop_duplicates(subset='Id')
    df = df.drop_duplicates(subset='Concatenados')
    df.to_csv('dados/dados_filtrados2.csv', sep=';', index=False)