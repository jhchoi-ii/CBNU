import json
import urllib.parse
import boto3

print('Loading function')


def detect_faces(bucket, key):
    s3 = boto3.client('rekognition')
    # response = s3.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':key}},Attributes=['ALL'])
    response = s3.detect_faces(Image={"S3Object":{ "Bucket" : bucket, "Name" : key}})
    return response

# def detect_labels(bucket, key):
#     s3 = boto3.client('rekognition')
#     response = s3.detect_labels(Image={"S3Object"}:{"Bucket":bucket, "Name":key})
#     return response
    
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        # response = s3.get_object(Bucket=bucket, Key=key)
        # print("CONTENT TYPE: " + response['ContentType'])
        # return response['ContentType']
        response = detect_faces(bucket, key)
        print(response)
    except Exception as e:
        print(e)
        # print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        # raise e