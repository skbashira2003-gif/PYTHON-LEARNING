import pandas as pd

# 1. Series
a = pd.Series([10, 20, 30, 40])
print(a)

# 2. DataFrame
data = {
    "Name": ["Ravi", "Bashira", "Rakesh"],
    "Age": [22, 23, 25],
    "Marks": [85, 95, 90]
}

df = pd.DataFrame(data)
print(df)

# 3. View Data
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# 4. Select Columns
print(df["Name"])
print(df[["Name", "Marks"]])

# 5. Select Rows
print(df.loc[0])
print(df.iloc[1])

# 6. Filtering
print(df[df["Marks"] > 85])

# 7. Add Column
df["City"] = ["Guntur", "Guntur", "Hyderabad"]
print(df)

# 8. Update Value
df.loc[0, "Marks"] = 90
print(df)

# 9. Delete Column
df = df.drop("City", axis=1)
print(df)

# 10. Sorting
print(df.sort_values("Marks"))
print(df.sort_values("Marks", ascending=False))

# 11. Statistics
print(df["Marks"].sum())
print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())

# 12. Missing Values
df.loc[1, "Marks"] = None
print(df.isnull())
print(df.isnull().sum())
df["Marks"] = df["Marks"].fillna(0)
print(df)

# 13. GroupBy
print(df.groupby("Age")["Marks"].mean())

# 14. Remove Duplicates
df = df.drop_duplicates()
print(df)

# 15. Save CSV
df.to_csv("students.csv", index=False)

# 16. Read CSV
data = pd.read_csv("students.csv")
print(data)