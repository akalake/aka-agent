import boto3
import os
from boto3.dynamodb.conditions import Key, Attr
s3 = boto3.client('s3')

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
REGION_NAME = os.getenv("REGION_NAME")

class S3Upload(object):
    def __init__(self):
        pass

    def upload_file_to_s3(self, file, file_path, bucket_name=S3_BUCKET_NAME, acl="public-read"):
        S3_LOCATION = "http://{}.s3.amazonaws.com/{}".format(S3_BUCKET_NAME, file_path)
        try:
            data = s3.upload_fileobj(
                file,
                bucket_name,
                file_path,
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type
                }
            )
            return S3_LOCATION
        except Exception as e:
            return e
