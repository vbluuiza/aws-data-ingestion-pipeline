
import boto3
from io import BytesIO
from dotenv import load_dotenv
from aws.session import get_s3_client
import os

load_dotenv()
bucket =  os.getenv('s3_bucket')

def upload_df_to_s3_parquet(df, bucket, s3_path):
    # Converte um DataFrame em parquet na memória e faz upload para S3.
    
    # Converte para parquet em memória
    buffer = BytesIO()
    df.to_parquet(buffer, index=False)
    buffer.seek(0)
    
    s3 =  get_s3_client()
    s3.upload_fileobj(buffer, bucket, s3_path)
    print(f"[✔] Send to s3://{bucket}/{s3_path}")
    