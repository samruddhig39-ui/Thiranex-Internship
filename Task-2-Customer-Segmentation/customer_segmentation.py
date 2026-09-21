
# CUSTOMER SEGMENTATION PROJECT
# Thiranex Data Analytics Internship - Task 2


# 1. IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# 2. LOAD DATASET

data = pd.read_csv("Mall_Customers.csv")

print("Dataset loaded successfully!\n")

print("First 5 rows:")
print(data.head())


# 3. CHECK THE DATA

print("\nDataset information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())


# 4. SELECT FEATURES FOR CLUSTERING

# We will use income and spending score
# to understand customer behaviour.

customer_data = data[
    ["Annual Income (k$)", "Spending Score (1-100)"]
]

# 5. ELBOW METHOD

# We test different numbers of clusters.

inertia = []

for number in range(1, 11):

    model = KMeans(
        n_clusters=number,
        random_state=42,
        n_init=10
    )

    model.fit(customer_data)

    inertia.append(model.inertia_)


# Create the Elbow graph

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, 11),
    inertia,
    marker="o"
)

plt.title("Elbow Method for Finding Number of Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")

plt.savefig("elbow_method.png")

plt.show()

# 6. CREATE K-MEANS MODEL
# From the Elbow Method, we use 5 clusters.

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)


# 7. CREATE CUSTOMER SEGMENTS

clusters = kmeans.fit_predict(customer_data)


# Add cluster number to our original dataset

data["Cluster"] = clusters


# 8. COUNT CUSTOMERS IN EACH SEGMENT

print("\nNumber of customers in each cluster:")

cluster_count = data["Cluster"].value_counts().sort_index()

print(cluster_count)


# 9. ANALYZE EACH CUSTOMER SEGMENT

cluster_summary = data.groupby("Cluster")[
    [
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
].mean()


print("\nAverage values for each cluster:")

print(cluster_summary)


# Save cluster summary

cluster_summary.to_csv(
    "Customer_Cluster_Summary.csv"
)

# 10. CUSTOMER SEGMENTATION VISUALIZATION

plt.figure(figsize=(9, 6))

plt.scatter(
    data["Annual Income (k$)"],
    data["Spending Score (1-100)"],
    c=data["Cluster"],
    s=70
)

plt.title("Customer Segmentation")

plt.xlabel("Annual Income (k$)")

plt.ylabel("Spending Score (1-100)")

plt.savefig(
    "customer_segmentation.png"
)

plt.show()


# 11. SAVE FINAL DATASET

data.to_csv(
    "Customer_Segmentation_Result.csv",
    index=False
)

# 12. PROJECT COMPLETED

print("CUSTOMER SEGMENTATION COMPLETED!")

print("\nFiles created:")

print("1. Customer_Segmentation_Result.csv")
print("2. Customer_Cluster_Summary.csv")
print("3. elbow_method.png")
print("4. customer_segmentation.png")