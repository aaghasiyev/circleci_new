from datetime import date
print("Hello from python to circleci")
import os
print(os.environ['CIRCLE_REPOSITORY_URL'])
today = date.today()
print("Today's date:", today)
