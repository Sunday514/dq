import read
import numpy as np
from collections import Counter

data = read.load_data()
print(data.head())
s = ""
for st in data["headline"]:
    if st is not np.NaN:
        s += st + ' '
lst = s.lower().split()
c = Counter(lst)
print (c.most_common(100))
