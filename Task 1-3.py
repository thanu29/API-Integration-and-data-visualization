# Visualize  the individual data in the dataset

# Extract all tags
all_tags = []
for item in data_API:
    all_tags.extend(item.get('tags', []))

# Count tags
tag_counts = Counter(all_tags)

# Plot tags
plt.figure(figsize=(8, 4))
sns.barplot(x=list(tag_counts.keys()), y=list(tag_counts.values()))
plt.title('Frequency of Tags')
plt.xlabel('Tags')
plt.ylabel('Count')
plt.show()

# Extract all categories
all_categories = []
for item in data_API:
    all_categories.extend(item.get('categories', []))

# Count categories
category_counts = Counter(all_categories)

# Plot categories
plt.figure(figsize=(8, 4))
sns.barplot(x=list(category_counts.keys()), y=list(category_counts.values()))
plt.title('Frequency of Categories')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.show()
# Extract all titles
all_titles = []
for item in data_API:
    all_titles.extend(item.get('title', []))

# Count title
title_counts = Counter(all_titles)

# Plot title
plt.figure(figsize=(12, 6))
sns.barplot(x=list(title_counts.keys()), y=list(title_counts.values()))
plt.title('Frequency of Titles')
plt.xlabel('Titles')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
