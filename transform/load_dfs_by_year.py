from config.setup_path import *
import pandas as pd
import os
from dotenv import load_dotenv
from s3_upload.upload_parquet import upload_df_to_s3_parquet

load_dotenv()

# Diretório onde estão os arquivos .csv
raw_dir = Path('data/raw')

# Lista de arquivos .csv ordenados alfabeticamente (ex: data_2015.csv, ...)
files = sorted(raw_dir.glob('*.csv'))


def load_csvs_by_year(files):
    dfs = {}
    for file in files:
        try:
            # Extrai o ano do nome do arquivo (ex: data_2015.csv → '2015')
            year = file.stem.split("_")[-1]
            dfs[year] = pd.read_csv(file, low_memory=False)
        except Exception as e:
            print(e)
            
    return dfs

dfs = load_csvs_by_year(files)

# Percorre todos os DataFrames organizados por ano
for year, df in dfs.items():
    # Define o caminho de destino no bucket S3 (camada bronze)
    path = f'bronze/data_{year}.parquet'
    bucket =  os.getenv('s3_bucket')
    # Faz upload do DataFrame convertido em Parquet diretamente para o S3
    upload_df_to_s3_parquet(df, bucket, path)
    print(f"Uploaded {year} ✔")

