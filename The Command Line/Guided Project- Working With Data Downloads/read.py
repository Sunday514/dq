import pandas as pd

contents = pd.read_csv("data/CRDC2013_14content.csv")

if __name__ == "__main__":
    print(contents.head())