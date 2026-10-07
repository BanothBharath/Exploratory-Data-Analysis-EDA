# Exploratory Data Analysis - Titanic Dataset

## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on a custom Titanic dataset using Python. The objective is to understand the dataset, identify patterns and relationships between variables, analyze data distributions, and visualize important insights.

The project uses Pandas for data analysis, Matplotlib and Seaborn for data visualization.

## 🎯 Objectives

- Load and understand the Titanic dataset
- Explore the structure and statistical characteristics of the data
- Identify missing values
- Analyze relationships between numerical features
- Study the distribution of important variables
- Visualize correlations using a heatmap
- Analyze relationships using scatterplots and boxplots
- Generate useful observations from the dataset

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

## 📂 Project Structure

```text
Exploratory-Data-Analysis-EDA/
│
├── EDA.py
├── custom_titanic_dataset.csv
├── custom_titanic_heatmap_fixed.png
├── custom_titanic_histograms.png
├── custom_titanic_scatterplot_fixed.png
└── README.md

🔍 Analysis Performed
1. Dataset Loading
The dataset is loaded using Pandas:
data = pd.read_csv('custom_titanic_dataset.csv')


2. Dataset Information
The project examines:
- Dataset structure
- First few records
- Descriptive statistics
- Numerical features
3. Missing Value Analysis
Missing values are checked for each column to understand data completeness.
4. Correlation Analysis
A correlation heatmap is generated to identify relationships between numerical variables.
Important correlations observed include:
- PassengerId and Fare: -0.25
- PassengerId and SibSp: 0.30
- PassengerId and Survived: 0.18
- Survived and SibSp: 0.19
- Survived and Parch: 0.19
- Survived and Fare: -0.15
Most other relationships are relatively weak.
5. Histograms
Histograms are used to understand the distributions of:
- PassengerId
- Survived
- Pclass
- Age
- SibSp
- Parch
- Fare
6. Scatterplot Analysis
An Age vs. Fare scatterplot is created with survival status represented using different markers/colors.
This helps visualize whether there is an apparent relationship between passenger age, fare, and survival.
7. Boxplot Analysis
The project also analyzes the distribution of Age according to survival status using a boxplot.
📊 Visualizations
The project generates the following visualizations:
- Correlation Heatmap
- Histograms
- Age vs. Fare Scatterplot
- Age Distribution by Survival Status
- Pairplot
💡 Key Observations
1. The correlation heatmap shows that most numerical variables have weak correlations with each other.
2. PassengerId has a relatively weak positive correlation with Survived.
3. Fare shows a weak negative correlation with Survived in this dataset.
4. Histograms provide an overview of the distribution of numerical variables.
5. The scatterplot helps visualize the relationship between Age and Fare while considering survival status.
6. The boxplot can be used to compare age distributions between passengers who survived and those who did not.
▶️ How to Run
Step 1: Clone the repository
git clone <YOUR-GITHUB-REPOSITORY-URL>

Step 2: Navigate to the project folder
cd Exploratory-Data-Analysis-EDA

Step 3: Install required libraries
pip install pandas matplotlib seaborn

Step 4: Run the Python script
python EDA.py

📋 Requirements
pandas
matplotlib
seaborn

👨‍💻 Author
Banoth Bharath
GitHub: BanothBharath
