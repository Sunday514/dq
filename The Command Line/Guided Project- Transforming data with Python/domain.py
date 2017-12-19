import read

data = read.load_data()
domains = data["url"].value_counts().order(ascending=False)
for name, row in domains[0:100].items():
    print("{0}: {1}".format(name, row))
    