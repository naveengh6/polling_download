import boto3
import boto3.session
import os
from config import settings
import traceback

# s3_ec_read_user
access_key = '<REPLACE ME>' # replace with access key
access_secret = '<REPLACE ME>' # replace with secret name
bucket = '<REPLACE ME>' # replace the bucket name

# paths
local_path = 'F:\\Development\\Github\\polling_download\\all' # replace this path from your local folder location

def downloadFromS3():
    settings.LOGGER.info('starting the download')
    i = 1
    try:
        mysession = boto3.session.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=access_secret
            )

        s3 = mysession.resource('s3')

        bucket = s3.Bucket(bucket)

        
        for fileobj in bucket.objects.all():
            filepath = os.path.dirname(fileobj.key)
            # print(filepath)
            # print(fileobj.key)
            if not os.path.exists(os.path.join(local_path, filepath)):
                os.makedirs(os.path.join(local_path, filepath))
            if len(str(fileobj.key).split('.')) > 1:
                bucket.download_file(fileobj.key, f'{local_path}\\{fileobj.key}')
                settings.LOGGER.info(f'downloaded files: {i}')
                i += 1
        settings.LOGGER.info('completed the download')
    except Exception as ex:
        settings.LOGGER.error(ex)
        traceback.print_exc()
        
if __name__ == '__main__':
    downloadFromS3()