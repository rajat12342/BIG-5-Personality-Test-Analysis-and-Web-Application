#This script moves all the data from a single column into multiple columns for readability and usability.

import pandas as pd

df = pd.read_csv("C:/Users/chich/Desktop/BIG5 Personality Project/data.csv", sep = "\t" )

print(df.head())

df.to_csv("C:/Users/chich/Desktop/BIG5 Personality Project/formatted_data.csv", index= False)


