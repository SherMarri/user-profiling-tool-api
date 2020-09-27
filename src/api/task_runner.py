import os
import re
from celery import Celery
from datetime import datetime

from . import exceptions


class TaskRunner:
  
  _APP_NAME = os.getenv('USER_PROFILER_CELERY_APP_NAME')
  _BROKER = os.getenv('USER_PROFILER_CELERY_BROKER_URL')
  _QUEUE = os.getenv('USER_PROFILER_CELERY_QUEUE')
  _TASK = os.getenv('USER_PROFILER_CELERY_TASK_NAME')
  _FORMAT = "%Y-%m-%d"


  def _init_celery(self):
    try:
      self._app = Celery(self._APP_NAME, broker=self._BROKER)
    except Exception as e:
      raise exceptions.CeleryInitException(str(e))
  
  def profile_users(self, dataset: str, email: str, from_date: str, to_date: str):
    self._validate(dataset, email, from_date, to_date)
    self._init_celery()
    kwargs = {
      'dataset': dataset,
      'email': email,
      'from_date': from_date,
      'to_date': to_date
    }
    try:
      self._app.send_task(self._TASK, kwargs=kwargs, queue=self._QUEUE)
    except Exception as e:
      raise exceptions.CelerySendTaskException(str(e))
  
  def _validate(self, dataset: str, email: str, from_date: str, to_date: str):
    self._validate_dataset(dataset)
    self._validate_email(email)
    self._validate_date_range(from_date, to_date)
  
  def _validate_dataset(self, dataset: str):
    if dataset is None:
      raise ValueError('"dataset" cannot be None.')
    if not isinstance(dataset, str):
      raise TypeError('"dataset" must be of type str.')
    if len(dataset) == 0:
      raise ValueError('"dataset" cannot be empty.')

  def _validate_email(self, email: str):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not email_regex.fullmatch(email):
      raise exceptions.InvalidEmailException
  
  def _validate_date_range(self, start_date: str, end_date: str):
    self._validate_date_format(start_date)
    self._validate_date_format(end_date)
    start = datetime.strptime(start_date, self._FORMAT)
    end = datetime.strptime(end_date, self._FORMAT)

    if start >= end:
      raise exceptions.InvalidDateRangeException
  
  def _validate_date_format(self, date: str):
    try:
      date = datetime.strptime(date, self._FORMAT)
    except Exception as e:
      raise exceptions.InvalidDateFormatException
