# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
df.head(5)

sns.catplot(y= "PayloadMass", x= "FlightNumber", hue= "Class", data= df, aspect= 5)
plt.xlabel("Flight Number", fontsize= 20)
plt.ylabel("Pay load Mass (kg)", fontsize= 20)
plt.show()

# Visualize the relationship between Flight Number and Launch Site
# Plot a scatter point chart with x axis to be Flight Number and y axis to be the launch site, and hue to be the class value
sns.catplot(y= "LaunchSite", x= "FlightNumber", hue= "Class", data= df, aspect= 5)
plt.xlabel("Flight Number", fontsize= 20)
plt.ylabel("Launch Site", fontsize= 20)
plt.show()

# Visualize the relationship between Payload and Launch Site
# Plot a scatter point chart with x-axis to be Pay Load Mass (kg) and y-axis to be the launchSite, and hue to be the class value
sns.scatterplot(y= "LaunchSite", x= "PayloadMass", hue= "Class", data= df)
plt.xlabel("Pay load Mass (kg)", fontsize= 20)
plt.ylabel("Launch Site", fontsize= 20)
plt.show()

# Visualize the relationship between success rate of each orbit type
mean_Orbit = df.groupby(by= "Orbit")['Class'].mean()
mean_Orbit.plot(kind='bar',figsize=(10, 6))
plt.xlabel('Orbit')
plt.ylabel('Class')
plt.title('relationship between success rate of each orbit type')
plt.show()

# Visualize the relationship between FlightNumber and Orbit type
# Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value
sns.scatterplot(y="Orbit", x="FlightNumber", hue= "Class", data = df)
plt.show()

# Visualize the relationship between Payload and Orbit type
# Plot a scatter point chart with x axis to be Payload and y axis to be the Orbit, and hue to be the class value
sns.scatterplot(y="Orbit", x="PayloadMass", hue= "Class", data = df)
plt.show()

features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()

# Create dummy variables to categorical columns
# Use get_dummies() function on the categorical columns
features_one_hot = pd.get_dummies(features)

# Export the dataset
features_one_hot.to_csv('dataset_part_3.csv', index=False)
