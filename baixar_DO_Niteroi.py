# Salva os Diários Oficiais da Prefeitura de Niteroi em pasta local

import os
from urllib.request import urlretrieve
from urllib.error import URLError

download_path = r'C:\DO_Niteroi'

# Mapeamento de mês para três letras
meses = {
    1: 'Jan',
    2: 'Fev',
    3: 'Mar',
    4: 'Abr',
    5: 'Mai',
    6: 'Jun',
    7: 'Jul',
    8: 'Ago',
    9: 'Set',
    10: 'Out',
    11: 'Nov',
    12: 'Dez'
}

# 'Loop' para totos os anos, meses e dias (não se sabe em quais dias houve publicação de DO)
for ano in range(2003, 2024):
    for mes in range(1, 13):
        for dia in range(1, 32):
            # Cria a URL
            url = f"https://www.niteroi.rj.gov.br/wp-content/uploads/do/{ano}/{str(mes).zfill(2)}_{meses[mes]}/{str(dia).zfill(2)}.pdf"
            print(url)

            # Criar o nome do arquivo
            nome_arquivo = f"{ano}_{str(mes).zfill(2)}_{str(dia).zfill(2)}.pdf"

            # Verificar se o arquivo já existe na pasta local (caso seja reexecutado)
            if not os.path.isfile(os.path.join(download_path, nome_arquivo)):
                # Se o arquivo não existir, tenta baixar e salvar
                try:
                    urlretrieve(url, os.path.join(download_path, nome_arquivo))
                except URLError:
                    # Se houver um erro ao baixar o arquivo (não existe DO naquele dia), passa para o próximo dia
                    continue