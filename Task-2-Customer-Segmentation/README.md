# Thiranex Internship - Task 2
## Customer Segmentation

### Project Overview

This project was developed as part of my Thiranex Data Analytics Internship.

The objective of this project is to segment customers based on their annual income and spending behavior using K-Means clustering.

### Dataset

The project uses the Mall Customers dataset containing customer demographic and spending information.

Main features:

- Customer ID
- Genre
- Age
- Annual Income
- Spending Score

### Methodology

1. Loaded and examined the dataset
2. Checked for missing values
3. Selected Annual Income and Spending Score for clustering
4. Used the Elbow Method to determine the number of clusters
5. Applied K-Means clustering
6. Analyzed the characteristics of each customer segment
7. Created visualizations of the customer segments
8. Exported the clustering results

### Customer Segments

The analysis identified five customer segments:

- Medium Income + Medium Spending
- High Income + High Spending
- Low Income + High Spending
- High Income + Low Spending
- Low Income + Low Spending

### Tools Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- K-Means Clustering

### Project Files

- `customer_segmentation.py` - Python source code
- `Mall_Customers.csv` - Dataset
- `Customer_Segmentation_Result.csv` - Dataset with cluster assignments
- `Customer_Cluster_Summary.csv` - Average characteristics of each cluster
- `elbow_method.png` - Elbow Method visualization
- `customer_segmentation.png` - Customer segmentation visualization

### Key Insights

- Customers with high income and high spending represent an important customer segment.
- Some high-income customers have relatively low spending scores.
- Some low-income customers have relatively high spending scores.
- Customers can be grouped into distinct segments based on income and spending behavior.

### Outcome

The project demonstrates the use of K-Means clustering for customer segmentation and provides insights that can support customer-focused marketing and business analysis.
