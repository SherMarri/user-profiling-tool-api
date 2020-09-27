class InvalidEmailException(Exception):
  """
  Should be raised for an invalid email address.
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'InvalidEmailException, {self.message}'
    else:
      return 'InvalidEmailException: This is not a valid email address.'


class CeleryInitException(Exception):
  """
  Should be raised when celery app fails to initialize.
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'CeleryInitException, {self.message}'
    else:
      return 'CeleryInitException: Failed to initialize celery app.'


class CelerySendTaskException(Exception):
  """
  Should be raised when celery app fails to send a task to broker.
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'CelerySendTaskException, {self.message}'
    else:
      return 'CelerySendTaskException: Failed to send task.'


class InvalidDateFormatException(Exception):
  """
  Should be raised for an invalid date format.
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'InvalidDateFormatException, {self.message}'
    else:
      return 'InvalidDateFormatException: This is not a valid date format.'


class InvalidDateRangeException(Exception):
  """
  Should be raised for an invalid date range.
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'InvalidDateRangeException, {self.message}'
    else:
      return 'InvalidDateRangeException: This is not a valid date range.'