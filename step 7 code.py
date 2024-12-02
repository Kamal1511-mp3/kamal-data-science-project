# Scatter plot matrix to analyze relationships between features
sns.pairplot(iris, hue='species', markers=["o", "s", "D"], palette="Set1")
plt.show()
