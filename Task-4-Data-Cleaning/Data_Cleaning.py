import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATASET

data = pd.read_csv("Messy_Sales_Data.csv")

print("Original Data:")
print(data.head())

print("\nOriginal number of rows:", len(data))


# CHECK MISSING VALUES


print("\nMissing Values:")
print(data.isnull().sum())


# REMOVE DUPLICATE ROWS

data = data.drop_duplicates()

print("\nRows after removing duplicates:", len(data))


# CLEAN TEXT COLUMNS

data["Customer_Name"] = data["Customer_Name"].str.strip()

data["City"] = data["City"].str.strip().str.title()

data["Product"] = data["Product"].str.strip().str.title()


# CLEAN DATE COLUMN

data["Order_Date"] = pd.to_datetime(
    data["Order_Date"],
    errors="coerce"
)


# HANDLE MISSING SALES VALUES

data["Sales"] = data["Sales"].fillna(
    data["Sales"].median()
)


# HANDLE OTHER MISSING VALUES

data["Customer_Name"] = data["Customer_Name"].fillna(
    "Unknown"
)

data["City"] = data["City"].fillna(
    "Unknown"
)

data["Product"] = data["Product"].fillna(
    "Unknown"
)


# CHECK CLEANED DATA

print("\nCleaned Data:")
print(data.head())

print("\nMissing values after cleaning:")
print(data.isnull().sum())


# SAVE CLEANED DATA

data.to_csv(
    "Cleaned_Sales_Data.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")


# CREATE SUMMARY REPORT

total_sales = data["Sales"].sum()

total_quantity = data["Quantity"].sum()

number_of_orders = data["Order_ID"].nunique()

average_sales = data["Sales"].mean()


print("SALES SUMMARY")

print("Total Sales:", round(total_sales, 2))

print("Total Quantity:", total_quantity)

print("Number of Orders:", number_of_orders)

print("Average Sales:", round(average_sales, 2))


# CREATE SALES BY CITY REPORT

city_sales = data.groupby(
    "City"
)["Sales"].sum().sort_values(
    ascending=False
)

print("\nSales by City:")
print(city_sales)


city_sales.to_csv(
    "Sales_By_City.csv"
)


# CREATE VISUAL REPORT

plt.figure(figsize=(8, 5))

city_sales.plot(
    kind="bar"
)

plt.title("Sales by City")

plt.xlabel("City")

plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "Sales_By_City.png"
)

plt.show()


# PROJECT COMPLETED

print("PYTHON CLEANING COMPLETED!")

print("\nFiles created:")

print("1. Cleaned_Sales_Data.csv")
print("2. Sales_By_City.csv")
print("3. Sales_By_City.png")