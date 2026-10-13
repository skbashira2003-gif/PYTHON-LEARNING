import pandas as pd


#  Creating Series

a = pd.Series([10, 20, 30, 40, 50])

b = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

print(a)
print(b)

print(type(a))

#  Creating DataFrames

df = pd.DataFrame({
    "Name": ["Bashira", "Ravi", "Priya", "Arun"],
    "Age": [23, 25, 24, 27],
    "City": ["Guntur", "Hyderabad", "Vijayawada", "Chennai"],
    "Salary": [25000, 30000, 28000, 35000]
})

print(df)

print(type(df))

#  DataFrame Properties

print("Shape:", df.shape)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("Columns:", df.columns)
print("Index:", df.index)

print("Data Types:")
print(df.dtypes)

print("Size:", df.size)

#  Viewing Data

print(df.head())

print(df.head(2))

print(df.tail())

print(df.tail(2))

print(df.info())

print(df.describe())

#  Selecting Columns

print(df["Name"])

print(df["Salary"])

print(df[["Name", "Salary"]])

print(df[["Name", "City", "Salary"]])

#  Selecting Rows

print(df.iloc[0])

print(df.iloc[1])

print(df.iloc[0:3])

print(df.iloc[[0, 2]])

#  loc and iloc

print(df.loc[0])

print(df.loc[0:2])

print(df.iloc[0:2])

print(df.iloc[0:2, 0:2])

#  Filtering Data

print(df[df["Age"] > 24])

print(df[df["Salary"] > 28000])

print(df[df["City"] == "Hyderabad"])

print(df[df["Salary"] < 30000])


# Multiple Conditions

print(df[(df["Age"] > 23) & (df["Salary"] > 27000)])

print(df[(df["Age"] > 23) | (df["Salary"] > 30000)])

#  Adding New Columns

df["Experience"] = [1, 2, 3, 4]

print(df)

df["Annual_Salary"] = df["Salary"] * 12

print(df)

#  Updating Data

df.loc[0, "Salary"] = 30000

print(df)

#  Removing Columns

df2 = df.drop("Experience", axis=1)

print(df2)

df3 = df.drop(columns=["Experience", "Annual_Salary"])

print(df3)

# Sorting Data

print(df.sort_values("Salary"))

print(df.sort_values("Salary", ascending=False))

print(df.sort_values("Age"))

#  Basic Calculations

print("Total Salary:", df["Salary"].sum())

print("Average Salary:", df["Salary"].mean())

print("Maximum Salary:", df["Salary"].max())

print("Minimum Salary:", df["Salary"].min())

print("Average Age:", df["Age"].mean())

print("Maximum Age:", df["Age"].max())

print("Minimum Age:", df["Age"].min())

#  Unique Values

print(df["City"].unique())

print(df["City"].nunique())

print(df["City"].value_counts())


# Missing Values

data = {
    "Name": ["Bashira", "Ravi", "Priya", "Arun"],
    "Age": [23, None, 24, 27],
    "Salary": [25000, 30000, None, 35000]
}

df_missing = pd.DataFrame(data)

print(df_missing)

print(df_missing.isnull())

print(df_missing.isnull().sum())

#  Fill Missing Values

df_missing["Age"] = df_missing["Age"].fillna(25)

df_missing["Salary"] = df_missing["Salary"].fillna(
    df_missing["Salary"].mean()
)

print(df_missing)


# Drop Missing Values


df_drop = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [20, None, 25]
})

print(df_drop)

print(df_drop.dropna())


#  Duplicate Values


data = {
    "Name": ["Bashira", "Ravi", "Bashira", "Priya"],
    "Age": [23, 25, 23, 24]
}

df_duplicate = pd.DataFrame(data)

print(df_duplicate)

print(df_duplicate.duplicated())

print(df_duplicate.drop_duplicates())



# 19. Rename Columns


df_rename = df.rename(
    columns={
        "Name": "Employee_Name",
        "Salary": "Monthly_Salary"
    }
)

print(df_rename)



#  GroupBy


data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Department": [
        "IT",
        "HR",
        "IT",
        "HR",
        "Sales"
    ],
    "Salary": [
        30000,
        25000,
        40000,
        28000,
        35000
    ]
}

df_group = pd.DataFrame(data)

print(df_group)

print(df_group.groupby("Department")["Salary"].mean())

print(df_group.groupby("Department")["Salary"].sum())

print(df_group.groupby("Department")["Salary"].max())




#  Apply Function


df["Salary_After_Bonus"] = df["Salary"].apply(
    lambda x: x + 5000
)

print(df)


#  Conditional Column


df["Status"] = df["Salary"].apply(
    lambda x: "High" if x >= 30000 else "Low"
)

print(df)


#  String Operations


df["Name_Upper"] = df["Name"].str.upper()

print(df)

df["Name_Lower"] = df["Name"].str.lower()

print(df)

#  Reset Index

df_reset = df.reset_index(drop=True)

print(df_reset)

#  Concatenation

df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Age": [20, 21]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Age": [22, 23]
})

result = pd.concat([df1, df2], ignore_index=True)

print(result)


#  Final Data Analysis

print("Employee Count:", len(df))

print("Average Salary:", df["Salary"].mean())

print("Highest Salary:", df["Salary"].max())

print("Lowest Salary:", df["Salary"].min())

print("Employees with Salary > 30000:")

print(df[df["Salary"] > 30000])