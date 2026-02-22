import pandas as pd

employees = {
    "Name": ["John","Jack","Mary"],
    "Age": [22,23,24],
    "Gender": ["Male","Female", "Non-binary"],
}

indices = []
index = 0
for employee in employees:
    index+=1;
    indices.append(f"Employee {index}")

df = pd.DataFrame(employees, index=indices)


# add salary as well for each
df["Salary"] = [50000,100000,200000]


print(df)

print("--------------------------------")

# get john's details
print(df.loc['Employee 1'])

print("--------------------------------")

# get jack's details
print(df.iloc[1])

print("--------------------------------")

print("New employees added!")
newRow = pd.DataFrame(
    [{
        "Name": "Jim",
        "Age": 22,
        "Gender": "Male",
        "Salary": 50000
    },
        {
            "Name": "Joe",
            "Age": 23,
            "Gender": "Female",
            "Salary": 10000
        }],
    index=["Employee 4","Employee 5"]
)

df = pd.concat([df, newRow])
print(df)



