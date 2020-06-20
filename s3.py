import boto3
from boto.s3.connection import S3Connection
import argparse


region = "eu-central-1.amazonaws.com"

def s3_save_file(file_path, s3_path, AWSAccessKeyId, AWSSecretKey, bucket_name):
    s3 = boto3.client('s3', aws_access_key_id=AWSAccessKeyId, aws_secret_access_key=AWSSecretKey)
    s3.upload_file(file_path, bucket_name, s3_path)

def s3_download_files(AWSAccessKeyId, AWSSecretKey, bucket_name):
  conn = S3Connection(AWSAccessKeyId, AWSSecretKey, host=region)
  conn.auth_region_name = region
  bucket = conn.get_bucket(bucket_name)
  for key in bucket.list():
      try:
          res = key.get_contents_to_filename(key.name)
      except:
          print(key.name+":"+"FAILED")



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='SSV')
    parser.add_argument('--AWSAccessKeyId', type=str, help='AWSAccessKeyId')
    parser.add_argument('--AWSSecretKey', type=str, help='AWSSecretKey')
    parser.add_argument('--bucket_name', type=str, help='bucket_name')
    parser.add_argument('--path', type=str, help='path')

    args = parser.parse_args()
    # ------------------------------------------------------------------------------------------------------------------------------------#

    s3_download_files(args.AWSAccessKeyId, args.AWSSecretKey, args.bucket_name)
    s3_save_file(args.path, 'ssv/dataset.tar.gz', args.AWSAccessKeyId, args.AWSSecretKey, args.bucket_name)
