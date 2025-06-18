
import boto3
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()
bucket =  os.getenv('s3_bucket')

# Converte um DataFrame em parquet na memória e faz upload para S3.
def upload_df_to_s3_parquet(df, bucket, s3_path):
    session = boto3.Session(profile_name='default') 
    s3 = session.client('s3')
    
    # Converte para parquet em memória
    buffer = BytesIO()
    df.to_parquet(buffer, index=False)
    buffer.seek(0)
    
    
    s3.upload_fileobj(buffer, bucket, s3_path)
    print(f"[✔] Send to s3://{bucket}/{s3_path}")
    