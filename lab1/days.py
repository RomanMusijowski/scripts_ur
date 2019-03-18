import sys
import datetime

date = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')
today = datetime.datetime.today()
days = date - today

print(days)
