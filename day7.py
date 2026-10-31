import pandas as pd

# DAY 7 - PANDAS DATA CLEANING

# CREATE SAMPLE DATASET

data = {
    "Name": [" Rahul ", "PRIYA", "Amit", "Rahul", None, "Sneha"],
    "Age": ["25", "30", None, "25", "28", "32"],
    "Salary": [30000, 40000, 35000, 30000, None, 45000],
    "Department": ["IT", "hr", "Sales", "IT", "HR ", "sales"],
    "Joining_Date": ["2024-01-10", "2023-05-15", "2024-03-20",
                     "2024-01-10", "2023-08-12", "2022-11-05"]
}

df = pd.DataFrame(data)

# DISPLAY ORIGINAL DATASET

print("ORIGINAL DATASET")
print(df)

# CHECK MISSING VALUES

print("\nMISSING VALUES")
print(df.isnull().sum())

# HANDLE MISSING VALUES

df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mode()[0])
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nDATA AFTER HANDLING MISSING VALUES")
print(df)

# CHECK DUPLICATE RECORDS

print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

# REMOVE DUPLICATE RECORDS

df = df.drop_duplicates()

print("\nDATA AFTER REMOVING DUPLICATES")
print(df)

# CORRECT DATA TYPES

df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(float)

print("\nDATA TYPES")
print(df.dtypes)

# STANDARDIZE TEXT CATEGORIES

df["Name"] = df["Name"].str.strip().str.title()

df["Department"] = df["Department"].str.strip().str.title()

print("\nSTANDARDIZED DATA")
print(df)

# CONVERT DATE INTO DATETIME

df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    errors="coerce"
)

print("\nDATE DATA TYPE")
print(df["Joining_Date"].dtype)

# CHECK DATA AFTER CLEANING

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\nDUPLICATES AFTER CLEANING")
print(df.duplicated().sum())

# COMPARE BEFORE AND AFTER CLEANING

print("\nFINAL DATASET")
print(df)

print("\nFINAL ROWS AND COLUMNS")
print(df.shape)

# SAVE CLEANED DATASET

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully.")