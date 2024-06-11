import boto3
import os

def load(dir, bucket_name, s3_prefix=''):
    s3_client = boto3.client('s3')

    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.join(s3_prefix, os.path.relpath(file_path, dir)).replace("\\", "/")
            try:
                s3_client.upload_file(file_path, bucket_name, s3_key)
                print('Load thành công lên S3')
            except FileNotFoundError:
                print('Không thành công')

local_directory = r'c:\Users\NITRO 5\Documents\Dev\DE\DWH'
s3_bucket_name = 'customerdataetl'
s3_folder_prefix = '' 

load(local_directory, s3_bucket_name, s3_folder_prefix)

