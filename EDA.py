import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('custom_titanic_dataset.csv')

# Display basic dataset information
print("Dataset Info:")
data.info()

print("\nFirst 5 rows:")
print(data.head())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Visualizations
sns.set(style="whitegrid")

# Pairplot
print("\nGenerating pairplot...")
sns.pairplot(data, diag_kind='kde', plot_kws={'alpha':0.6})
plt.show()

# Heatmap of correlations
print("\nGenerating heatmap...")
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Histogram for numerical columns
print("\nGenerating histograms...")
data.hist(bins=30, figsize=(15, 10), color='blue', edgecolor='black')
plt.suptitle('Histograms of Numerical Features')
plt.show()

# Boxplot for age vs. survival
if 'Age' in data.columns and 'Survived' in data.columns:
    print("\nGenerating boxplot for Age vs. Survival...")
    sns.boxplot(x='Survived', y='Age', data=data, palette="Set2")
    plt.title('Age Distribution by Survival Status')
    plt.show()

# Scatterplot for Fare vs. Age
if 'Fare' in data.columns and 'Age' in data.columns:
    print("\nGenerating scatterplot for Fare vs. Age...")
    sns.scatterplot(x='Fare', y='Age', hue='Survived', data=data, palette="coolwarm")
    plt.title('Fare vs. Age with Survival Status')
    plt.show()

# Observations and summary
print("\nObservations:")
print("1. The correlation heatmap shows relationships between features.")
print("2. Histograms provide insights into the distribution of numerical features.")
print("3. Pairplots and scatterplots help identify trends and relationships.")
print("4. Boxplots reveal differences in age distributions between survival statuses.")

# Save findings to a PDF report
with open('eda_summary.txt', 'w') as f:
    f.write("Exploratory Data Analysis Summary\n")
    f.write("================================\n\n")
    f.write("Dataset Information:\n")
    data.info(buf=f)
    f.write("\n\nDescriptive Statistics:\n")
    f.write(data.describe().to_string())
    f.write("\n\nMissing Values:\n")
    f.write(data.isnull().sum().to_string())
    f.write("\n\nObservations:\n")
    f.write("1. The correlation heatmap shows relationships between features.\n")
    f.write("2. Histograms provide insights into the distribution of numerical features.\n")
    f.write("3. Pairplots and scatterplots help identify trends and relationships.\n")
    f.write("4. Boxplots reveal differences in age distributions between survival statuses.\n")

print("EDA completed and summary saved to 'eda_summary.txt'.")
