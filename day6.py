
# PANDAS

#1 Import Pandas
import pandas as pd

print("Pandas imported successfully")


# LOADING DATASETS

#1 Create a sample dataset
data = {
    "name": ["Ritesh", "Rahul", "Amit", "Priya", "Sneha"],
    "age": [23, 25, 22, 24, 26],
    "salary": [25000, 30000, 28000, 35000, 32000],
    "department": ["IT", "HR", "IT", "Sales", "HR"]
}

df = pd.DataFrame(data)

print(df)


#2 Load CSV file
df = pd.read_csv("employees.csv")

print(df)


#3 Load Excel file
df = pd.read_excel("employees.xlsx")

print(df)


# DATASET EXPLORATION

#1 Display first five rows
df = pd.read_csv("employees.csv")

print(df.head())


#2 Display last five rows
print(df.tail())


#3 Display first three rows
print(df.head(3))


#4 Display dataset information
df.info()


#5 Display statistical information
print(df.describe())


# ROWS AND COLUMNS

#1 Count total rows
print("Total rows:", df.shape[0])


#2 Count total columns
print("Total columns:", df.shape[1])


#3 Display column names
print("Column names:", df.columns)


#4 Display data types
print(df.dtypes)


#5 Display dataset shape
print("Dataset shape:", df.shape)


# COLUMN SELECTION

#1 Select one column
print(df["name"])


#2 Select multiple columns
print(df[["name", "salary"]])


#3 Select salary column
print(df["salary"])


# MISSING VALUES

#1 Check missing values
print(df.isnull())


#2 Count missing values
print(df.isnull().sum())


#3 Check total missing values
print("Total missing values:", df.isnull().sum().sum())


# DATA QUALITY CHECKING

#1 Check duplicate records
print("Duplicate records:", df.duplicated().sum())


#2 Display duplicate records
print(df[df.duplicated()])


#3 Check unique values in department
print(df["department"].unique())


#4 Count department categories
print(df["department"].value_counts())


# DATA DICTIONARY

#1 Create data dictionary
data_dictionary = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Description": [
        "Employee name",
        "Employee age",
        "Employee salary",
        "Employee department"
    ]
})

print(data_dictionary)


#2 Save data dictionary to CSV
data_dictionary.to_csv("data_dictionary.csv", index=False)

print("Data dictionary saved successfully")
