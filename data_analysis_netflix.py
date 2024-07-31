import pandas as pd

# Load the dataset
file_path = 'C:/Users/DELL/Downloads/netflix_data.csv'
netflix_data = pd.read_csv(file_path)

# Display the first few rows and summary information
netflix_data.head(), netflix_data.info(), netflix_data.describe(include='all')


# Data cleaning: Handling missing values

# Fill missing 'director' and 'cast' values with 'Unknown'
netflix_data['director'].fillna('Unknown', inplace=True)
netflix_data['cast'].fillna('Unknown', inplace=True)

# Fill missing 'country' values with 'Unknown'
netflix_data['country'].fillna('Unknown', inplace=True)

# Fill missing 'date_added' values with 'Unknown'
netflix_data['date_added'].fillna('Unknown', inplace=True)

# Fill missing 'rating' values with 'Not Rated'
netflix_data['rating'].fillna('Not Rated', inplace=True)

# Verify that there are no missing values left
missing_values = netflix_data.isnull().sum()

# Save the cleaned dataset
cleaned_file_path = 'C:/Users/DELL/Downloads/Netflix_shows_movies.csv'
netflix_data.to_csv(cleaned_file_path, index=False)

missing_values, cleaned_file_path


import seaborn as sns
import matplotlib.pyplot as plt

# Data exploration: Descriptive statistics and visualizations

# Distribution of 'type' (Movies vs. TV Shows)
type_counts = netflix_data['type'].value_counts()
type_counts

# Plot the distribution of 'type'
plt.figure(figsize=(6, 4))
sns.countplot(data=netflix_data, x='type', palette='viridis')
plt.title('Distribution of Content Type')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Distribution of ratings
rating_counts = netflix_data['rating'].value_counts()
rating_counts

# Plot the distribution of ratings
plt.figure(figsize=(10, 6))
sns.countplot(data=netflix_data, x='rating', order=rating_counts.index, palette='muted')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Most common genres
genre_counts = netflix_data['listed_in'].str.split(', ').explode().value_counts()
genre_counts

# Plot the most common genres
plt.figure(figsize=(12, 8))
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='coolwarm')
plt.title('Most Common Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()


# Saving the 'Most Common Genres' plot data for R integration

# Extract the genre counts data
genre_counts_df = genre_counts.reset_index()
genre_counts_df.columns = ['genre', 'count']

# Save as a CSV file for use in R
genre_counts_file_path = 'C:/Users/DELL/Downloads/most_common_genres.csv'
genre_counts_df.to_csv(genre_counts_file_path, index=False)

genre_counts_file_path
