# Thiranex Internship - Task 4
## Data Cleaning & Reporting Automation

### Project Overview

This project was developed as part of my Thiranex Data Analytics Internship.

The objective of this project is to automate the data cleaning and reporting process using Python.

The project takes a messy sales dataset, cleans the data, handles missing values and duplicates, and generates automated summary reports and visualizations.

### Dataset

The dataset contains sales information with the following columns:

- Order ID
- Customer Name
- City
- Order Date
- Product
- Quantity
- Sales

The dataset intentionally contains common data quality issues such as:

- Missing values
- Duplicate records
- Extra spaces
- Inconsistent city names and capitalization
- Different date formats

### Data Cleaning Process

The Python script performs the following steps:

1. Loads the CSV dataset using Pandas.
2. Checks the dataset and missing values.
3. Removes duplicate records.
4. Removes unnecessary spaces from text values.
5. Standardizes city and product names.
6. Converts the Order Date column into a proper date format.
7. Handles missing Sales values using the median.
8. Replaces missing text values with "Unknown".
9. Checks the cleaned dataset.
10. Saves the cleaned dataset as a new CSV file.

### Automated Reporting

The script automatically generates:

- Total Sales
- Total Quantity
- Number of Orders
- Average Sales
- Sales by City

A CSV report containing sales by city is also generated.

### Visualization

A bar chart is automatically created to visualize:

**Sales by City**

The visualization is saved as:

`Sales_By_City.png`

### Tools Used

- Python
- Pandas
- Matplotlib

### Project Files

- `task4_python_cleaning.py` - Python automation script
- `Task4_Messy_Sales_Data.csv` - Original messy dataset
- `Cleaned_Sales_Data.csv` - Cleaned dataset
- `Sales_By_City.csv` - Automated city-wise sales report
- `Sales_By_City.png` - Sales visualization
- `README.md` - Project documentation

### Key Insights

- Data cleaning improves the consistency and reliability of the dataset.
- Duplicate records can affect sales calculations and therefore need to be removed.
- Standardizing city and product names makes grouping and reporting more accurate.
- Missing sales values can be handled using an appropriate statistical value such as the median.
- Automated reports reduce the need for repetitive manual calculations.

### Outcome

This project demonstrates a basic automated data cleaning and reporting workflow using Python.

It provides practical experience in data preprocessing, missing-value handling, duplicate removal, data standardization, automated reporting and data visualization.
