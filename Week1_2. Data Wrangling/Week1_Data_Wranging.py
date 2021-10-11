# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321ENSkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)

df.isnull().sum() / df.count() * 100

df.dtypes

# Apply value_counts() on column LaunchSite
df['LaunchSite'].value_counts()

# Apply value_counts on Orbit column
df['Orbit'].value_counts()

# landing_outcomes = values on Outcome column
landing_outcomes = df['Outcome'].value_counts()

for i, outcome in enumerate(landing_outcomes.keys()):
    print(i, outcome)

bad_outcomes = set(landing_outcomes.keys()[[1, 3, 5, 6, 7]])
bad_outcomes

# landing_class = 0 if bad_outcome
# landing_class = 1 otherwise
landing_class = []
for i in df['Outcome']:
    if i in bad_outcomes:
        landing_class.append(int(0))
    else:
        landing_class.append(int(1))

df['Class'] = landing_class
df[['Class']].head(8)

df.head(5)

df["Class"].mean()