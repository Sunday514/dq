import dateutil
import read

def ex_hour(s):
    dt = dateutil.parser.parse(s)
    return dt.hour

data = read.load_data()
shour = data["submission_time"].apply(ex_hour)
nhour = shour.value_counts()
print(nhour)
