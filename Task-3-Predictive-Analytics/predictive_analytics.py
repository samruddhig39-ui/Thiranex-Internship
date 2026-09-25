# PREDICTIVE ANALYTICS USING HISTORICAL DATA
# Thiranex Data Analytics Internship - Task 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# LOAD DATASET

data = pd.read_csv("Superstore.csv",encoding="latin1")

print("Dataset loaded successfully!\n")

print("First 5 rows:")
print(data.head())


# CHECK DATA

print("\nDataset information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())


# PREPARE DATE COLUMN

data["Order Date"] = pd.to_datetime(
    data["Order Date"],
    errors="coerce"
)

data = data.dropna(
    subset=["Order Date", "Sales"]
)


# CREATE MONTHLY SALES DATA

monthly_sales = (
    data.groupby(
        pd.Grouper(
            key="Order Date",
            freq="MS"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

monthly_sales.columns = [
    "Date",
    "Sales"
]


# 5. CREATE MONTH NUMBER

monthly_sales["Month_Number"] = range(
    1,
    len(monthly_sales) + 1
)


print("\nMonthly Sales:")
print(monthly_sales.head())


# SPLIT DATA INTO TRAINING AND TESTING

test_size = 12

train_data = monthly_sales.iloc[:-test_size]

test_data = monthly_sales.iloc[-test_size:]


X_train = train_data[
    ["Month_Number"]
]

y_train = train_data[
    "Sales"
]

X_test = test_data[
    ["Month_Number"]
]

y_test = test_data[
    "Sales"
]


# CREATE LINEAR REGRESSION MODEL

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

# PREDICT TEST DATA

test_predictions = model.predict(
    X_test
)


# EVALUATE MODEL

mae = mean_absolute_error(
    y_test,
    test_predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        test_predictions
    )
)

r2 = r2_score(
    y_test,
    test_predictions
)

print("MODEL EVALUATION")

print("Mean Absolute Error:", round(mae, 2))

print("Root Mean Squared Error:", round(rmse, 2))

print("R2 Score:", round(r2, 2))


# SAVE TEST PREDICTIONS

prediction_results = test_data[
    ["Date", "Sales"]
].copy()

prediction_results[
    "Predicted Sales"
] = test_predictions


prediction_results.to_csv(
    "Sales_Forecast_Result.csv",
    index=False
)


# VISUALIZE ACTUAL VS PREDICTED SALES

plt.figure(figsize=(10, 6))

plt.plot(
    test_data["Date"],
    y_test,
    marker="o",
    label="Actual Sales"
)

plt.plot(
    test_data["Date"],
    test_predictions,
    marker="o",
    label="Predicted Sales"
)

plt.title(
    "Actual vs Predicted Sales"
)

plt.xlabel("Date")

plt.ylabel("Sales")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "model_predictions.png"
)

plt.show()


# FORECAST NEXT 12 MONTHS

future_dates = pd.date_range(
    start=monthly_sales["Date"].max()
    + pd.offsets.MonthBegin(1),
    periods=12,
    freq="MS"
)


future_month_numbers = range(
    len(monthly_sales) + 1,
    len(monthly_sales) + 13
)


future_data = pd.DataFrame(
    {
        "Month_Number": future_month_numbers
    }
)


future_predictions = model.predict(
    future_data[
        ["Month_Number"]
    ]
)


future_forecast = pd.DataFrame(
    {
        "Date": future_dates,
        "Forecasted Sales": future_predictions
    }
)


# SAVE FUTURE FORECAST

future_forecast.to_csv(
    "Future_Sales_Forecast.csv",
    index=False
)


print("\nNext 12 Months Sales Forecast:")

print(future_forecast)


# VISUALIZE FUTURE FORECAST

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_sales["Date"],
    monthly_sales["Sales"],
    marker="o",
    label="Historical Sales"
)

plt.plot(
    future_forecast["Date"],
    future_forecast["Forecasted Sales"],
    marker="o",
    linestyle="--",
    label="Future Forecast"
)

plt.title(
    "Future Sales Forecast"
)

plt.xlabel("Date")

plt.ylabel("Sales")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "future_forecast.png"
)

plt.show()


# PROJECT COMPLETED

print("PREDICTIVE ANALYTICS COMPLETED!")

print("\nFiles created:")

print("1. Sales_Forecast_Result.csv")

print("2. Future_Sales_Forecast.csv")

print("3. model_predictions.png")

print("4. future_forecast.png")