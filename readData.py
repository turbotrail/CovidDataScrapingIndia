from time import time
import pandas as pd
import requests
import io
from datetime import timedelta
from datetime import datetime
state="Tamil Nadu"
url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/date.csv"
def caseCount(time):
    urlLatest=url.replace("date",time.strftime('%m-%d-%Y'))
    downloadLatest = requests.get(urlLatest).content
    dfLatest = pd.read_csv(io.StringIO(downloadLatest.decode('utf-8')),index_col ="Province_State")
    count=dfLatest.loc[state]["Confirmed"]
    return count
timeHourNow=int(datetime.now().strftime('%H'))    
if(timeHourNow>=00 and timeHourNow<=10):
    current_time = datetime.now() - timedelta(days = 2)
    oldTime=datetime.now() - timedelta(days = 3)
    olderTime=datetime.now() - timedelta(days = 4)
else:
    current_time = datetime.now() - timedelta(days = 1)
    oldTime=datetime.now() - timedelta(days = 2)
    olderTime=datetime.now() - timedelta(days = 3)
# print(datetime.utcnow().strftime('%H'))

newCases=caseCount(current_time)-caseCount(oldTime)
oldCases=caseCount(oldTime)-caseCount(olderTime)
print("Yesterday's case:"+ str(oldCases))
print("Today's case:"+ str(newCases))
print("Percentage Increase in cases in "+state+" :")
increase=((newCases-oldCases)/oldCases)*100
print(str(increase)+"%")


