demonstration, I'll use the Iris dataset, which is a popular dataset in machine learning and statistics. It contains 150 samples of iris flowers, with four features (sepal length, sepal width, petal length, and petal width) and a target variable (species).

We will:

Load the data.
Perform basic summary statistics.
Explore distributions, correlations, and potential outliers.
Visualize findings using histograms, scatter plots, and heatmaps.

Step 1: Load the Dataset
First, let's load the dataset and display the first few rows.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from seaborn's built-in dataset collection
iris = sns.load_dataset('iris')

# Display the first few rows
iris.head()


Step 2: Data Overview
We'll check for basic statistics and any missing data.

# Summary statistics
iris.describe()

# Check for missing values
iris.isnull().sum()


Step 3: Explore Feature Distributions
We'll examine the distribution of the features using histograms.

# Plot histograms of each feature
iris.drop('species', axis=1).hist(figsize=(10, 8), bins=20, color='lightblue', edgecolor='black')
plt.tight_layout()
plt.show()
