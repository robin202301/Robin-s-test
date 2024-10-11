import pandas as pd

# Load the test dataset
data = pd.read_csv('robin_demo.csv')

# Function to check for unexpected strings in a specific column
def check_unexpected_strings(df, column, expected_strings):
    unexpected = df[~df[column].isin(expected_strings)]
    return unexpected

# Function to check for unexpected numerical values
def check_unexpected_numerical(df, column, min_value, max_value):
    unexpected = df[(df[column] < min_value) | (df[column] > max_value)]
    return unexpected

# Function to check for unexpected dates
def check_unexpected_dates(df, column, start_date, end_date):
    unexpected = df[(df[column] < pd.to_datetime(start_date)) | (df[column] > pd.to_datetime(end_date))]
    return unexpected

# Check for unexpected strings in 'category' column
expected_categories = ['A', 'B', 'C', 'D']
unexpected_strings = check_unexpected_strings(data, 'category', expected_categories)

# Check for unexpected numerical values in 'value' column
unexpected_numerical = check_unexpected_numerical(data, 'value', 0, 100)

# Check for unexpected dates in 'date' column
unexpected_dates = check_unexpected_dates(data, 'date', '2020-01-01', '2024-12-31')

# Check for data integrity (example: join with another dataframe)
reference_data = pd.read_csv('reference_data.csv')
merged_data = data.merge(reference_data, on='id', how='left', indicator=True)
missing_reference = merged_data[merged_data['_merge'] == 'left_only']

# Edge case investigation: Check for duplicates
duplicates = data[data.duplicated()]

# Output the results
print("Unexpected Strings:")
print(unexpected_strings)

print("\nUnexpected Numerical Values:")
print(unexpected_numerical)

print("\nUnexpected Dates:")
print(unexpected_dates)

print("\nMissing Reference Data:")
print(missing_reference)

print("\nDuplicates:")
print(duplicates)

# Robin's Conclusions On data quality
"""
1. Unexpected Strings: Presence of unexpected categories may indicate data entry errors
   or new categories that need to be added to the expected list.
   
2. Unexpected Numerical Values: Values outside the expected range suggest potential
   data entry errors or outliers that need further investigation.
   
3. Unexpected Dates: Dates outside the specified range may indicate data entry mistakes,
   misformatted dates, or entries that shouldn't exist (e.g., future dates).
   
4. Missing Reference Data: Rows with missing references indicate potential integrity issues
   when joining datasets, warranting a review of data sources and relationships.
   
5. Duplicates: Duplicate entries could reflect data quality issues that need to be addressed
   to ensure the uniqueness and accuracy of the dataset.
"""
