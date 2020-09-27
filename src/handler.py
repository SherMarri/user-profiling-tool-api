import os
import json
import traceback

from src import settings
from src.api import TaskRunner, exceptions

def response(code, data):
  return {
    'statusCode': code,
    'headers': {
        'content-type': 'application/json; charset=utf-8'
    },
    'body': json.dumps(data)
  }


def validate_inputs(inputs):
  if 'dataset' not in inputs:
    raise KeyError('dataset is missing')
  
  if 'email' not in inputs:
    raise KeyError('email is missing')
  
  if 'from_date' not in inputs:
    raise KeyError('email is missing')

  if 'to_date' not in inputs:
    raise KeyError('email is missing')
  
  dataset = inputs['dataset']
  email = inputs['email']
  from_date = inputs['from_date']
  to_date = inputs['to_date']
  return dataset, email, from_date, to_date


def send_task(event, context):
  try:
    body = json.loads(event['body'])
    dataset, email, from_date, to_date = validate_inputs(body)
    task_runner = TaskRunner()
    task_runner.profile_users(dataset, email, from_date, to_date)
    return response(200, 'Queued.')
  except (KeyError, exceptions.InvalidEmailException) as e:
    return response(422, {'message': str(e)})
  except Exception as e:
    print(e)
    traceback.print_exc()
    return response(500, {'message': 'Something unexpected occurred. Please check your request or try again later.'})
