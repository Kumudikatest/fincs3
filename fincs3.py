import boto3
translate = boto3.client("translate")
s3 = boto3.client("s3")

def handler(request):
   
    try:
        data = s3.list_objects(
            Bucket="cloud9-ktest",
            MaxKeys=10
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    
    return "Successfully executed"
