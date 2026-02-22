# aggregate functions: reduces a group of
#   values into a single summary value;
#   used to analyze and summarize data;
#   often used with the groupBy() function
import pandas as pd

users = pd.read_csv("data.csv")


# WHole Dataframe
print(users.mean(numeric_only=True))
print("-------------------\n")
print(users.max(numeric_only=True))
print("-------------------\n")
print(users.count())
print("-------------------\n")


#Single Column

print(users['age'].mean())
print("-------------------\n")
print(users['id'].min())
print("-------------------\n")
print(users['age'].std())

