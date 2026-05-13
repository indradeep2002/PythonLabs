import pandas as pd 
import numpy as np 

data = {

    "Name": ["Amit", "Sohan", "Rajesh", "Rik", "Rahul", "Anup", "Sagar", "Sneha"], 
    "Age": [21, 22, 23, 24, 25, 26, 27, 28],
    "Marks": [85, 90, 95, 91, 75, 56, 71, 87],

}

df = pd.DataFrame(data)

print(df)
print()

print(df.head())
print()
print(df.shape)
print()
print(df.describe())
print()

avg_marks = np.mean(df["Marks"])
print(avg_marks)
print()

print(np.max(df["Marks"]))
print()

print(np.min(df["Marks"]))
