# Laptop Price Analytics Dashboard

## About the Project

This project is a simple data analytics project where I analyzed a laptop pricing dataset using Python, MySQL, and Power BI. The main goal was to understand how different factors such as brand, RAM, weight, and operating system affect laptop prices.

I first cleaned and processed the dataset using Python, stored the transformed data in MySQL, performed exploratory data analysis (EDA), and then created an interactive dashboard in Power BI to visualize the findings.

---

## Tools Used

* Python
* Pandas
* NumPy
* MySQL
* SQLAlchemy
* Matplotlib
* Seaborn
* Power BI

---

## Project Workflow

### 1. Data Cleaning and Preparation

* Loaded the dataset using Pandas.
* Converted laptop prices from Euros to INR.
* Extracted numerical values from RAM and Weight columns.
* Removed unnecessary formatting and prepared the data for analysis.

### 2. Database Integration

* Connected Python with MySQL using SQLAlchemy.
* Stored the cleaned dataset in MySQL.
* Retrieved data from MySQL for further analysis.

### 3. Data Analysis

Performed various analyses such as:

* Average laptop price by brand
* Laptop price distribution
* Correlation between RAM, weight, and price
* Top 5 most expensive laptops
* Operating system distribution
* Mid-range laptop filtering
* RAM vs Price analysis

### 4. Power BI Dashboard

Created a dashboard to visualize:

* Brand-wise price comparison
* Price distribution
* Operating system market share
* Hardware specification impact on pricing

---

## Visualizations

The following charts were created during the analysis:

* Average Price by Brand
* Price Distribution Histogram
* Correlation Heatmap
* Operating System Distribution
* RAM vs Price Scatter Plot
* Top 5 Most Expensive Laptops

---

## Project Structure

```text
Laptop-Price-Analysis/

├── .idea/
├── Power BI/
│   └── dashboard.png
├── data/
│   └── laptop_price.csv
├── images/
│   ├── avg_price_by_brand.png
│   ├── correlation_heatmap.png
│   ├── os_distribution.png
│   ├── price_distribution.png
│   ├── ram_vs_price.png
│   └── top5_expensive.png
├── README.md
├── filtered_laptops.csv
├── main.py
├── requirements.txt
└── rk.pbix
```

---
## Insights Generated

Through the analysis, the project explores:

- Brand-wise laptop pricing trends
- Price distribution across different laptops
- Relationship between hardware specifications and price
- Operating system distribution
- Identification of high-end and mid-range laptops

---

## Dashboard Preview

<img width="938" height="535" alt="dashboard" src="https://github.com/user-attachments/assets/5f71407b-eb69-49e2-81b0-1cb378550ccb" />


## Future Improvements

* Build a machine learning model to predict laptop prices.
* Add more interactive Power BI reports.
* Automate the data pipeline for larger datasets.

---

## Author

Rukesh

B.Tech (Artificial Intelligence)

This project was created to practice data cleaning, SQL integration, exploratory data analysis, and dashboard development using real-world data.
