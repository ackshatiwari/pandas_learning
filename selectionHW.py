import pandas as pd

# create a simple user program

df = pd.read_csv("data.csv", index_col = 'name')



name = input("Enter your name: ")
try:
    print(df.loc[name])
except KeyError:
    print(f"Sorry, {name} doesn't exist")

