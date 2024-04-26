import requests
import json
import boto3

def GetDataApi():
    response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
    data = response_API.json()  # Parse JSON directly into a dictionary
    return data

def save_to_s3(data, bucket_name, object_key, aws_access_key_id, aws_secret_access_key):
    # Initialize S3 client with provided credentials
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    # Convert data to JSON string
    json_data = json.dumps(data)

    # Upload data to S3 bucket
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=json_data)

# Main function to fetch data and save to S3
def main():
    data = GetDataApi()
    bucket_name = 'datafrompython'  # Replace with your S3 bucket name
    object_key = 'covid_data.json'  # Specify the key for the S3 object

    save_to_s3(data, bucket_name, object_key, aws_access_key_id, aws_secret_access_key)

if __name__ == "__main__":
    main()
