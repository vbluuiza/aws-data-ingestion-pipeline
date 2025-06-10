import boto3
from dotenv import load_dotenv
import os

def get_s3_client():
    # Carrega variáveis do .env, configura a sessão boto3 e retorna o cliente S3.
    load_dotenv()

    aws_access_key_id = os.getenv('aws_access_key_id')
    aws_secret_access_key = os.getenv('aws_secret_access_key')
    region_name = os.getenv('region_name')

    if not aws_access_key_id or not aws_secret_access_key:
        raise ValueError("❌ AWS credentials not found in environment variables.")
    
    boto3.setup_default_session(
        aws_access_key_id = aws_access_key_id, 
        aws_secret_access_key = aws_secret_access_key, 
        region_name = region_name,
        )

    s3 = boto3.client('s3')
    return s3
