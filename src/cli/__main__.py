import os
import sys
import traceback

from src import settings
from src.api import TaskRunner, exceptions


def parse_arguments():
  if len(sys.argv) != 5:
    print("Invalid number of arguments supplied.")
    print(f"Usage: python -m src.cli <dataset> <email> <from_date> <to_date>")
    raise SystemExit(f"Example: python -m src.cli my_dataset labs@citibeats.net 2020-08-01 2020-08-09")
  return sys.argv[1:] 


if __name__ == "__main__":
  dataset, email, from_date, to_date = parse_arguments()
  print(dataset, email, from_date, to_date)
  try:
    runner = TaskRunner()
    runner.profile_users(dataset, email, from_date, to_date)
  except Exception as err:
    print(str(err))
    traceback.print_exc()
