import kaggle
import boto3
from pathlib import Path

def download_dataset(ds:str, dwpath:str, filename:str) -> Path:
 kaggle.api.dataset_download_files(ds,dwpath,force=True,unzip=True)
 path = Path(f"{dwpath}/{filename}")
 return path

def write_cloud(path: Path) -> None:
    """Upload local parquet file to GCS"""
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )
    s3.upload_file(path.as_posix(), 'dtc-data-lake', path.as_posix())
    return

if __name__ == '__main__':
  path=download_dataset("jainilcoder/online-payment-fraud-detection",".","onlinefraud.csv")
  write_cloud(path)
