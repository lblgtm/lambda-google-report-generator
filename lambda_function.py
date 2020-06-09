import json
from google_report import GoogleReport

def lambda_handler(event, context):
    # TODO implement
    start_date = event["queryStringParameters"]["startDate"]
    end_date = event["queryStringParameters"]["endDate"]
    report = GoogleReport()
    resp = report.generate(start_date,end_date)
    return resp

