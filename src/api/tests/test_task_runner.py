import os
from unittest import TestCase
from celery import Celery

from src import settings
from src.api import TaskRunner, exceptions


class TestInitCelery(TestCase):
  
  def test_init_celery(self):
    runner = TaskRunner()
    runner._init_celery()
    self.assertIsNotNone(getattr(runner, '_app'))
    self.assertIsInstance(runner._app, Celery)


class TestValidateDataset(TestCase):
  
  def setUp(self):
    self.runner = TaskRunner()

  def test_none_key(self):
    with self.assertRaises(ValueError):
      self.runner._validate_dataset(None)
  
  def test_empty_key(self):
    with self.assertRaises(ValueError):
      self.runner._validate_dataset('')
  
  def test_invalid_type(self):
    with self.assertRaises(TypeError):
      self.runner._validate_dataset(1)
  
  def test_valid_key(self):
    result = self.runner._validate_dataset('my_dataset')
    self.assertIsNone(result)


class TestValidateEmail(TestCase):

  def setUp(self):
    self.runner = TaskRunner()
  
  def test_invalid_email(self):
    with self.assertRaises(exceptions.InvalidEmailException):
      self.runner._validate_email('asdasdasd')
  
  def test_valid_email(self):
    result = self.runner._validate_email('labs@citibeats.net')
    self.assertIsNone(result)


class TestValidateDateFormat(TestCase):

  def setUp(self):
    self.runner = TaskRunner()
  
  def test_valid_format(self):
    result = self.runner._validate_date_format('2020-06-01')
    self.assertIsNone(result)

  def test_invalid_format(self):
    with self.assertRaises(exceptions.InvalidDateFormatException):
      self.runner._validate_date_format('2020-14-33')


class TestValidateDateRange(TestCase):

  def setUp(self):
    self.runner = TaskRunner()
  
  def test_valid_range(self):
    result = self.runner._validate_date_range('2020-06-01', '2020-08-05')
    self.assertIsNone(result)

  def test_invalid_range(self):
    with self.assertRaises(exceptions.InvalidDateRangeException):
      self.runner._validate_date_range('2020-09-01', '2020-08-05')


class TestValidate(TestCase):

  def setUp(self):
    self.runner = TaskRunner()
  
  def test_none_dataset(self):
    with self.assertRaises(ValueError):
      self.runner._validate(None, 'labs@citibeats.net', '2020-08-01', '2020-08-06')
  
  def test_empty_dataset(self):
    with self.assertRaises(ValueError):
      self.runner._validate('', 'labs@citibeats.net', '2020-08-01', '2020-08-06')
  
  def test_invalid_dataset_type(self):
    with self.assertRaises(TypeError):
      self.runner._validate(1, 'labs@citibeats.net', '2020-08-01', '2020-08-06')
  
  def test_invalid_email(self):
    with self.assertRaises(exceptions.InvalidEmailException):
      self.runner._validate('my_dataset', 'labs.citibeats.net', '2020-08-01', '2020-08-06')
  
  def test_valid_email(self):
    result = self.runner._validate('my_dataset', 'labs@citibeats.net', '2020-08-01', '2020-08-06')
    self.assertIsNone(result)


class TestProfileUsers(TestCase):
  
  def setUp(self):
    self.runner = TaskRunner()
  
  def test_method(self):
    result = self.runner.profile_users('my_dataset', 'labs@citibeats.net', '2020-07-21', '2020-08-05')
    self.assertIsNone(result)
