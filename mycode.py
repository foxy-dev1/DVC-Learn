import os
import pandas as pd

data = {"name":["alice","bob","charlie","pop"],
        "age":[19,23,44,34],
        "city":["new york","los angeles","chicago","SF"]
       }

df = pd.DataFrame(data)


data_dir = "data"

os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,"sample_data.csv")

df.to_csv(file_path,index=False)

print(f"csv saved to path {file_path}")

