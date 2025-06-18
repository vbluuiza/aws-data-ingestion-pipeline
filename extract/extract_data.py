import requests
import os

def extract_data(url:str, filename:str) -> None:
    # Faz download de um arquivo CSV a partir de uma URL e salva localmente.

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Garante que o diretório de destino existe (cria se não existir)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            # Abre o arquivo no modo binário de escrita e salva o conteúdo
            with open(filename, 'wb') as f:
                f.write(response.content)
                print(f'File downloaded and saved as {filename}')
        else:
            print(f'Failed to download the file. Status code: {response.status_code}')

        print(f'Extracted {filename}')
    except Exception as e:
        print(e)
    
def run_extract():
    # Executa o processo de extração de múltiplas URLs e salva os arquivos.
    
    urls = [
    "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/c9509ab4-6f6d-4b97-979a-0cf2a10c922b/download/tmphrybkxuh.csv",
    "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/b7ea6b1b-3ca4-4c5b-9713-6dc1db52379a/download/tmpzxzxeqfb.csv",
    "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/30022137-709d-465e-baae-ca155b51927d/download/tmpzccn8u4q.csv",
    "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/2be28d90-3a90-4af1-a3f6-f28c1e25880a/download/tmp7602cia8.csv",
    "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/ea2e4696-4a2d-429c-9807-d02eb92e0222/download/tmpcje3ep_w.csv",
    "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/6ff6a6fd-3141-4440-a880-6f60a37fe789/download/tmpcv_10m2s.csv"
    ]

    filenames = [
    "data/raw/data_2015.csv",
    "data/raw/data_2016.csv",
    "data/raw/data_2017.csv",
    "data/raw/data_2018.csv",
    "data/raw/data_2019.csv",
    "data/raw/data_2020.csv"
    ]


    for url, filename in zip(urls, filenames):
        extract_data(url, filename)
        
        
run_extract()