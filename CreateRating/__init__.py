import logging

import azure.functions as func
import uuid
from datetime import datetime
import json


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        if 'productId' not in req_body:
            logging.error('Missing productId')
            return func.HttpResponse(f"Missing productId", status_code=400)
        if 'userId' not in req_body:
            logging.error('Missing userId')
            return func.HttpResponse(f"Missing userId", status_code=400)
        if 'rating' not in req_body:
            logging.error('Missing rating')
            return func.HttpResponse(f"Missing rating", status_code=400)
        if isinstance(req_body['rating'], int) is False:
            logging.error('Rating is not numeric')
            return func.HttpResponse(f"Rating is not numeric", status_code=400)
        if req_body['rating'] < 0 or req_body['rating'] > 5:
            logging.error('Rating out of range')
            return func.HttpResponse(f"Rating out of range", status_code=400)
    except ValueError:
        return func.HttpResponse(f"Invalid entry", status_code=500)

    data = {}
    for val in ['productId', 'userId', 'rating', 'locationName', 'userNotes']:
        if val in req_body:
            data[val] = req_body.get[val]
    
    data['id'] = str(uuid.uuid4())
    data['timestamp'] = datetime.utcnow().isoformat()
    doc.set(data)
    return func.HttpResponse(
         "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
         status_code=200
    )
