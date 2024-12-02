# Create box plots to identify potential outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=iris.drop('species', axis=1))
plt.title('Boxplots of Features')
plt.show()
