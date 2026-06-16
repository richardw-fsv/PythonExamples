import os

import boto3
import tempfile
import shutil
from pathlib import Path
'''
This module provides utility functions to interact with S3-compatible storage 
services, such as LocalStack's S3 service. It includes functions to create an 
S3 client, list buckets, and list objects within a bucket.
'''
def get_s3_client(endpoint_url='http://localhost:4566'):
    """
    Description
        Creates and returns an S3 client configured to connect to the specified endpoint URL.
    
    Args
        endpoint_url (str): 
            The URL of the S3 service endpoint. Default endpoint URL is 'http://localhost:4566' for LocalStack.
        
    Returns
        boto3.client: An S3 client instance.
    """
    try:
        return boto3.client('s3', endpoint_url=endpoint_url)  
    except Exception as e:
        raise ValueError(f"Error creating S3 client: {e}")

def list_s3_buckets(s3_client):
    '''
    Description
        Lists all S3 buckets available in the configured S3 service.
    
    Args
        s3_client (boto3.client): An S3 client instance.
    Returns
        list: A list of dictionaries, each representing an S3 bucket.
    '''
    try:
        return s3_client.list_buckets().get('Buckets', [])
    except Exception as e:
        raise ValueError(f"Error listing S3 buckets: {e}")
    
def list_s3_objects(s3_client, bucket_name):
    '''
    Description
        Lists all objects in the specified S3 bucket.
    Args
            s3_client (boto3.client): An S3 client instance.
            bucket_name (str): The name of the S3 bucket.
    Returns
        list: A list of dictionaries, each representing an S3 object.
    ''' 
    try:
        return s3_client.list_objects_v2(Bucket=bucket_name).get('Contents', [])
    except Exception as e:
        raise ValueError(f"Error listing objects in bucket '{bucket_name}': {e}")
    
def get_s3_object(s3_client, bucket_name, object_key):
    '''
    Description
        Retrieves the content of a specific object from an S3 bucket.
    Args
        s3_client (boto3.client): An S3 client instance.
        bucket_name (str): The name of the S3 bucket.
        object_key (str): The key of the S3 object to retrieve.
    Returns
        bytes: The content of the S3 object as bytes.
    '''
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        return response.get('Body').read()
    except Exception as e:
        raise ValueError(f"Error retrieving object '{object_key}' from bucket '{bucket_name}': {e}")

def backup_s3_objects(s3_client, backup_path=Path.home() / "s3_backup.zip"):
    '''
    Description
        Creates a backup of all objects in the specified S3 bucket by copying them to a new location with a given prefix.
    Args
        s3_client (boto3.client): An S3 client instance.
        bucket_name (str): The name of the S3 bucket to back up.
        backup_prefix (str): The prefix to use for the backup objects (e.g., 'backup/').
    Returns
        list: A list of dictionaries, each representing a backed-up S3 object.
    '''
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            print(f"Created temporary directory for backup: {temp_dir}")
            for bucket in list_s3_buckets(s3_client):
                bucket_name = bucket['Name']
                print(f"Bucket: {bucket_name}")
                folder_path = Path(temp_dir) / bucket_name
                folder_path.mkdir(parents=True, exist_ok=True)
                objects = list_s3_objects(s3_client, bucket_name)
                for obj in objects:
                    f = get_s3_object(s3_client, bucket_name, obj['Key'])
                    path = folder_path / obj['Key']
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(f)
                    print(f"Backed up object '{obj['Key']}' to '{path}'")
            print(f"Creating backup zip file: {backup_path}")
        
            shutil.make_archive(f"{backup_path.with_suffix('')}", 'zip', temp_dir)
            print(f"S3 backup created as {backup_path}")
        
    except Exception as e:
        raise ValueError(f"Error backing up objects in bucket '{bucket_name}': {e}")

def restore_s3_objects(s3_client, backup_path=Path.home() / "s3_backup.zip"):
    '''
    Description
        Restores objects from a backup zip file to the specified S3 bucket.
    Args
        s3_client (boto3.client): An S3 client instance.
        backup_path (Path): The path to the backup zip file containing the objects to restore.
    Returns
        None
    '''
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            print(f"Extracting backup zip file: {backup_path}")
            shutil.unpack_archive(str(backup_path), temp_dir)
            print(f"Extracted backup to temporary directory: {temp_dir}")
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = Path(root) / file
                    bucket_name = Path(root).relative_to(temp_dir).parts[0]
                    object_key = str(file_path.relative_to(Path(temp_dir) / bucket_name))
                    # with open(file_path, 'rb') as f:
                    #     s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=f.read())
                    print(f"Restored object '{object_key}' to bucket '{bucket_name}'")
            print("S3 restoration completed.")
        
    except Exception as e:
        raise ValueError(f"Error restoring objects from backup: {e}")

# Example usage
restore_s3_objects(get_s3_client(), Path("C:/Users/rcwes/OneDrive/Attachments/Desktop/s3_backup.zip"))
# s3_client = get_s3_client()
# print("S3 Buckets and their objects:")
# bucket_list = list_s3_buckets(s3_client)
# if not bucket_list:
#     print("No buckets found.")
#     exit(0)

# for bucket in bucket_list:
#     bucket_name = bucket['Name']
#     print(f"* {bucket_name}")
#     for obj in list_s3_objects(s3_client, bucket_name):
#         print(f"  - {obj['Key']}")
    
# doc = get_s3_object(s3_client, "projects", "aws/compose.yaml")
# print("\nContent of 'aws/compose.yaml':")
# print(doc.decode('utf-8'))

