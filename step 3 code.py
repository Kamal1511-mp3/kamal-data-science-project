# Plot histograms of each feature
iris.drop('species', axis=1).hist(figsize=(10, 8), bins=20, color='lightblue', edgecolor='black')
plt.tight_layout()
plt.show()
