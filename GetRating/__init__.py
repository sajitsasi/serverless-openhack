import logging

import azure.functions as func
import json

def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if len(doc) > 0:
        return func.HttpResponse(f"{json.dumps(doc[0].to_json())}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
