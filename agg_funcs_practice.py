import pandas as pd

def calc_z_score(user_age, avg_age, stdev):
    if stdev == 0:
        return 0.0

    z_score = (user_age - avg_age) / stdev
    return z_score


df = pd.read_csv("data.csv")

user_age = int(input("Enter age: "))

avg_age = df['age'].mean()

stdev = df['age'].std()

if(calc_z_score(user_age, avg_age, stdev) > 0):
    print(f"Your age was above the average age by {calc_z_score(user_age, avg_age, stdev)} z-score.")
else:
    print(f"Your age was below the average age by {abs(calc_z_score(user_age, avg_age, stdev))} z-score.")



