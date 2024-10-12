import pandas as pd 
import os 

data = {'Name' : ["Alice", "Bob", "Charlie"], 'Age' : [25 , 28 , 30]}
df = pd.DataFrame(data)
print(df)

data_dir = 'data'
os.makedirs(data_dir , exist_ok = True)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index= False)

print(f"The file has been saved to {file_path}")