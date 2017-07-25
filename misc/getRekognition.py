
from __future__ import print_function
import boto3
import json
import urllib
from wordcloud import WordCloud
import matplotlib.pyplot as plt

rekognition = boto3.client('rekognition')


def detect_labels(bucket, key):
    response = rekognition.detect_labels(Image={"S3Object": {"Bucket": bucket, "Name": key}})
    return response


def create_wordcloud(payload, key):
    keywords = ''
    json_obj = json.loads(payload)

    for i in json_obj['Labels']:
        for key, value in i.iteritems():
            if key == "Name":
                print(value)
                keywords += str(value) + ' '

    # Generate a word cloud image
    wc = WordCloud().generate(keywords)

    # Display the generated image:
    # the matplotlib way:
    plt.imshow(wc, interpolation='bilinear')
    keysplit = key.split('.')
    filename = keysplit[0] + '.png'
    wc.to_file('/tmp/' + filename)

    return filename


def push_to_sqs(body, bucket, key):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key
        }
    )
    json_dump = json.dumps(body)  # SQS MessageBody expects string, not dict
    sqs = boto3.client('sqs')
    try:
        response = sqs.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/831555608520/MetaMuleQueue',
            DelaySeconds=1,
            MessageBody=json_dump,
            MessageAttributes={
                'bucket': {
                    'DataType': 'String',
                    'StringValue': bucket
                },
                'key': {
                    'DataType': 'String',
                    'StringValue': key
                },
                'url': {
                    'DataType': 'String',
                    'StringValue': url
                }
            }
        )
    except Exception as e:
        print(e)
        raise e
    print(response)


def lambda_handler(event, context):
    # Demonstrates S3 trigger that uses Rekognition APIs to detect faces, labels and index faces in S3 Object.
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))

    try:
        # Calls rekognition DetectLabels API to detect labels in S3 object
        response = detect_labels(bucket, key)
        # Print response to console.
        print(response)
        worldcloud_key = create_wordcloud(response, key)
        s3_wc = boto3.client('s3')
        s3_wc.uploadfile('/tmp/' + worldcloud_key, 'ehog-wordclouds', worldcloud_key)
        push_to_sqs(response, bucket, key)

        return response
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket) +
              "Make sure your object and bucket exist and your bucket is in the same region as this function.")
        raise e
