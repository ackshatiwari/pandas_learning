import pandas as pd

df = pd.read_csv("data.csv", index_col = 'name')

# print(df["name"].to_string())

# print(df["age"].to_string())

# print(df[["name","age","country"]].to_string())

print(df.to_string())

print("----------------------\n")

print(df.loc['Tyler Fisher'])
