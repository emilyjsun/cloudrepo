import pandas as pd
# import boto3
# import os
import logging
from io import StringIO
LOG = logging.getLogger()
LOG.setLevel(logging.INFO)
logHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logHandler.setFormatter(formatter)
LOG.addHandler(logHandler)

def lambda_handler(event, context):
    try:
        # s3 = boto3.client('s3', aws_access_key_id=os.environ.get('ACCESS_KEY_ID'),
        #  aws_secret_access_key=os.environ.get('ACCESS_SECRET_KEY'))
        # LOG.info("s3 created")
        # 's3' is a key word. create connection to S3 using default config and all buckets within S3
        # bucket = 'cloudfbucket'
        file = "train/ds_salaries.csv"
        
        # obj = s3.get_object(Bucket= bucket, Key= file) 
            
        
        # get object and file (key) from bucket
        
        salaries = pd.read_csv(file)
        LOG.info("data read")
        
        LOG.info("start data cleaning")
        salaries_clean = clean_data(salaries)
        
        # LOG.info("write clean data to s3")
        
        with StringIO() as csv_buffer:
            salaries_clean.to_csv(csv_buffer, index=False)
        
            # response = s3.put_object(
            #     Bucket=bucket, Key="train/salaries_clean.csv", Body=csv_buffer.getvalue()
            # )
        
            # status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
        
            # if status == 200:
            #     return {'statusCode': 200, "body": {"message": "Success Cleaning Data"}}
            # else:
            #     return {'statusCode': status, "body": {"message": "Error writing to s3"}}
        
    except Exception as e:
        LOG.error("error while handling lambda event")
        return {'statusCode': 500, "body": {"message": "Failed", 'what': e}}
    
def clean_data(df):
    # create a copy of the dataframe
    df_clean = df.copy()
    # drop the first column
    df_clean = df_clean.drop(columns =['Unnamed: 0'])
    # rename some columns
    df_clean.rename(columns = {'employee_residence' : 'residence', 'work_year': 'year'}, inplace = True)
    # handle duplicate values
    df_clean.drop_duplicates(inplace=True)
    
    # create copy of the clean file
    df_cleaned = df_clean.copy()
    return df_cleaned