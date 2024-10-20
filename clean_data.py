# Mihir Kalyanthaya
# 10/20/24
# Assignment 06
import pandas as pd

df = pd.read_csv("C:/Users/mihir/OneDrive/Desktop/messy_population_data.csv")

print(df.info())
print("Before shape:", df.shape)

# data statistics
print(df.describe(include='all'))

# check missing values 
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# check duplicates
duplicates = df.duplicated().sum()
print(f'Duplicate rows: {duplicates}')

# check value_counts
print(df['income_groups'].value_counts())
print(df['age'].value_counts())
print(df['gender'].value_counts())
print(df['year'].value_counts())

# unique values
unique_counts = df.nunique()
unique_counts_df = unique_counts.reset_index()
unique_counts_df.columns = ['Column Name', 'Unique Count']
print(unique_counts_df)

###########################################
# cleaning the data
# remove age = 0, replace 1 and 2 with male and female, remove years after 2024
df = df[df['age'] != 0]
clean_df = df['gender'] = df['gender'].replace({1: 'male', 2: 'female'})
clean_df = df[df['year'] <= 2024]
clean_df.to_csv("C:/Users/mihir/OneDrive/Desktop/clean_population_data.csv", index=False)

print("Clean DF\n")
print(clean_df.info())
print(clean_df.describe(include='all'))

print("\nValue Counts for Categorical Columns:")
for column in clean_df.select_dtypes(include=['object']).columns:
    print(f"\nValue counts for '{column}':")
    print(clean_df[column].value_counts())

unique_counts = clean_df.nunique()
unique_counts_df = unique_counts.reset_index()
unique_counts_df.columns = ['Column Name', 'Unique Count']
print(unique_counts_df)
