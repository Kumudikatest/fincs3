import boto3
translate = boto3.client("translate")
s3 = boto3.client("s3")

def handler(request):
    try:
        data = translate.translate_text(
            SourceLanguageCode="auto",
            TargetLanguageCode="en",
            Text="hola"
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    
    return "Successfully executed"
