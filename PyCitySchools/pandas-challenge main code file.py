#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# Read the CSV files
schools = pd.read_csv(r'C:\Users\Tasnia Wahid\Downloads\Starter_Code (2)\Starter_Code\PyCitySchools\Resources\schools_complete.csv')
students = pd.read_csv(r'C:\Users\Tasnia Wahid\Downloads\Starter_Code (2)\Starter_Code\PyCitySchools\Resources\students_complete.csv')

# Merge the data on the common column 'school_name'
merged_data = pd.merge(students, schools, how="left", on=["school_name", "school_name"])

# District Summary calculations
total_schools = merged_data["school_name"].nunique()
total_students = merged_data["student_name"].count()
total_budget = schools["budget"].sum()
average_math_score = merged_data["math_score"].mean()
average_reading_score = merged_data["reading_score"].mean()

# Calculate the percentage passing math, reading, and overall passing
passing_math_percentage = (merged_data["math_score"] >= 70).mean() * 100
passing_reading_percentage = (merged_data["reading_score"] >= 70).mean() * 100
overall_passing_percentage = ((merged_data["math_score"] >= 70) & (merged_data["reading_score"] >= 70)).mean() * 100

# Create a District Summary DataFrame
district_summary = pd.DataFrame({
    "Total Schools": [total_schools],
    "Total Students": [total_students],
    "Total Budget": [total_budget],
    "Average Math Score": [average_math_score],
    "Average Reading Score": [average_reading_score],
    "% Passing Math": [passing_math_percentage],
    "% Passing Reading": [passing_reading_percentage],
    "% Overall Passing": [overall_passing_percentage]
})

# Display the District Summary
district_summary


# In[5]:


# Check the available column names in the merged DataFrame
print(merged_data.columns)


# In[12]:


# School Summary calculations
school_summary = school_group.agg({
    "type": "first",  # School type
    "student_name": "count",  # Total students
    "budget": "first",  # Total school budget
    "math_score": "mean",  # Average math score
    "reading_score": "mean",  # Average reading score
    "math_score": lambda x: (x >= 70).mean() * 100,  # Percentage passing math
    "reading_score": lambda x: (x >= 70).mean() * 100,  # Percentage passing reading
    "math_score": lambda x: ((x >= 70).sum(axis=0) >= 1).mean() * 100  # Percentage overall passing
})

# Rename columns
school_summary = school_summary.rename(columns={
    "type": "School Type",
    "student_name": "Total Students",
    "budget": "Total School Budget",
    "math_score": "Average Math Score",
    "reading_score": "Average Reading Score",
    "math_score": "% Passing Math",
    "reading_score": "% Passing Reading",
    "math_score": "% Overall Passing"
})

# Display the School Summary
school_summary


# In[13]:


# Sort the schools by % Overall Passing in descending order
top_schools = school_summary.sort_values(by="% Overall Passing", ascending=False)

# Display the top 5 rows
top_schools.head(5)


# In[14]:


# Sort the schools by % Overall Passing in ascending order
bottom_schools = school_summary.sort_values(by="% Overall Passing")

# Display the top 5 rows
bottom_schools.head(5)


# In[15]:


# Create a pivot table to show average math scores by grade and school
math_scores_by_grade = pd.pivot_table(merged_data, values='math_score', index='school_name', columns='grade', aggfunc='mean')

# Reorder columns to have grades in ascending order
math_scores_by_grade = math_scores_by_grade[['9th', '10th', '11th', '12th']]

# Display the DataFrame
math_scores_by_grade


# In[16]:


# Create a pivot table to show average reading scores by grade and school
reading_scores_by_grade = pd.pivot_table(merged_data, values='reading_score', index='school_name', columns='grade', aggfunc='mean')

# Reorder columns to have grades in ascending order
reading_scores_by_grade = reading_scores_by_grade[['9th', '10th', '11th', '12th']]

# Display the DataFrame
reading_scores_by_grade


# In[28]:


school_data_complete["Spending Ranges (Per Student)"] = pd.cut(
    school_data_complete["budget"] / school_data_complete["size"],
    spending_bins,
    labels=labels
)

# Group by spending ranges and calculate mean scores
spending_summary = school_data_complete.groupby("Spending Ranges (Per Student)").agg({
    "math_score": "mean",
    "reading_score": "mean",
    "% Passing Math": "mean",
    "% Passing Reading": "mean",
    "% Overall Passing": "mean"
}).reset_index()  # Resetting index to make Spending Ranges a regular column

# Rename columns
spending_summary = spending_summary.rename(columns={
    "math_score": "Average Math Score",
    "reading_score": "Average Reading Score",
    "% Passing Math": "% Passing Math",
    "% Passing Reading": "% Passing Reading",
    "% Overall Passing": "% Overall Passing"
})

# Display the DataFrame
spending_summary


# In[44]:


per_school_summary["Total Students"] = pd.to_numeric(per_school_summary["Total Students"], errors='coerce')

# Define the bins and labels for school size
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Add a new column to the DataFrame to categorize school size based on the bins
per_school_summary["School Size"] = pd.cut(per_school_summary["Total Students"], bins=size_bins, labels=labels)

# Group by school size and calculate mean scores
size_summary = per_school_summary.groupby("School Size").agg({
    "Average Math Score": "mean",
    "Average Reading Score": "mean",
    "% Passing Math": "mean",
    "% Passing Reading": "mean",
    "% Overall Passing": "mean"
}).reset_index()  # Resetting index to make School Size a regular column

# Display the size_summary DataFrame
size_summary


# In[47]:


# Group by school type and calculate mean scores
type_summary = per_school_summary.groupby("School Type").agg({
    "Average Math Score": "mean",
    "Average Reading Score": "mean",
    "% Passing Math": "mean",
    "% Passing Reading": "mean",
    "% Overall Passing": "mean"
}).reset_index()  # Resetting index to make School Type a regular column

# Display the type_summary DataFrame

print(per_school_summary.columns)



# In[ ]:




