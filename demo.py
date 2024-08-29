import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title("Data Intern Job Analysis")

# Loading data from the URL
url = 'https://raw.githubusercontent.com/zhenliferris/learing_streamlit/main/data/Data_salaries_modified.csv'
df = pd.read_csv(url)

# Display the data source information
st.header("Data source :green[Kaggle] :rocket: ")
st.write("https://www.kaggle.com/datasets/emreksz/data-science-and-analytics-internships-and-salaries/data")

st.header("Cleaned Data", divider="rainbow")
# Display the first 10 rows of the dataset
st.write(df.head(10))

# Analysis - Top  locations by job count
st.header("Top Locations by Job Counts", divider="rainbow")

num_location = st.slider("Choose the number of top locations to display", min_value=1, max_value=len(set(df['Location'])), value=5)

# Calculate job counts by location
loca_count = df['Location'].value_counts().reset_index()
loca_count.columns = ['Location', 'count']
loca_top = loca_count[:num_location]

# Sorting the DataFrame
loca_top = loca_top.sort_values(by='count', ascending=True)

# Plotting a horizontal bar chart
fig, ax = plt.subplots()
loca_top.plot.barh(x='Location', y='count', legend=False, ax=ax)

# Adding labels and title
ax.set_xlabel('Count')
ax.set_ylabel('Location')
ax.set_title(f'Top {num_location} Locations by Job Count')

# Display the plot in Streamlit
st.pyplot(fig)


st.header("Salary or Company score Distrubution", divider="rainbow")

# Dropdown to choose between 'Salary' or 'Company Score'
column_choice = st.selectbox("Choose the data to plot", ["Salary", "Company Score"])
num_bin = st.slider("Choose the number of bin", min_value=1, max_value=150, value=30)
# df['Salary'].plot.hist(bins=num_bin, edgecolor='black')
# plt.xlabel('Salary Distribution')
# plt.title('Histogram of Salary Data')
# rewrite the code for streamlit
fig, ax = plt.subplots()
ax.hist(df[column_choice], bins=num_bin, edgecolor='black')
ax.set_xlabel(f'{column_choice} Distribution')
ax.set_title(f'Histogram of {column_choice} Data')

# Display the plot in Streamlit
st.pyplot(fig)

st.header("Salary Vs Company score heatmap", divider="rainbow")

# correlation_matrix = df[['Company Score', 'Salary']].corr()
# # Plotting the heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation_matrix, annot=True, cmap='Reds', linewidths=.5)
# plt.title('Correaltion of Salary and Score')
# plt.show()

# rewrite the code for streamlit
# Calculate the correlation matrix
correlation_matrix = df[['Company Score', 'Salary']].corr()
# Plotting the heatmap using matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(correlation_matrix, cmap='Reds')
# Adding color bar
fig.colorbar(cax)

# Setting up ticks and labels
ax.set_xticks(np.arange(len(correlation_matrix.columns)))
ax.set_yticks(np.arange(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns)
ax.set_yticklabels(correlation_matrix.columns)

# Annotating the heatmap with the correlation values
for (i, j), val in np.ndenumerate(correlation_matrix.values):
    ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='black')

plt.title('Correlation of Salary and Score')

# Display the plot in Streamlit
st.pyplot(fig)

st.header("Top salary or score by locations or company", divider="rainbow")
# User selections
metric = st.selectbox("Choose the metric", ["Salary", "Company Score"])
group_by = st.selectbox("Group by", ["Location", "Company"])
top_n = st.slider("Select the number of top entries", min_value=1, max_value=50, value=10)

# Calculate the maximum values by the selected group
max_df = df.groupby(group_by)[metric].max()

# Sort and get the top N
top_n_df = max_df.sort_values(ascending=False).head(top_n).reset_index()
top_n_df = top_n_df.sort_values(by=metric, ascending=True)

# Plotting the bar chart
fig, ax = plt.subplots()
top_n_df.plot.barh(x=group_by, y=metric, ax=ax, legend=False, color='green')
ax.set_ylabel(group_by)
ax.set_xlabel(metric)
ax.set_title(f'Top {top_n} {metric} by {group_by}')

# Display the plot in Streamlit
st.pyplot(fig)

# st.header("", divider="rainbow")

# st.header("", divider="rainbow")
# st.header("", divider="rainbow")

# st.markdown("* _Step 1_")
# st.markdown("* _Step 2_")

# st.header("Two", divider=True)
# col1, col2 = st.columns(2)
# # with col1:
# #     x = st.slider("Choose an x value", 1,10)
# # with col2:
# #     st.write("the square of :red[**x**]is: ", x*x)

# st.header("Three", divider=True)
# st.write("This is a :red[book] text")

# st.header("Four", divider=True)



