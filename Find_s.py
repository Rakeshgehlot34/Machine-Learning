import numpy as np
import pandas as pd
df = pd.read_csv("D:\\Programs\\Machine-Learning\\Find_s_Data.csv")
print(df)
df.head()
df.shape
df.info()
features = np.array(df)[:,:-1]
target = np.array(df)[:,-1]
def find_s(fet,tar):
    final_list = []
    for i, val_tar in enumerate(tar):
        if val_tar == 1:
            current_hypothesis = list(fet[i])
            final_list.append(current_hypothesis)
        else:
            try:
                final_list.append(final_list[i-1])
            except:
                final_list = final_list         
    for i in range(1, len(final_list)):
        for j in range(0, len(final_list[i])):
            if final_list[i][j] != final_list[i-1][j]:
                final_list[i][j] = '?'
    return final_list[-1]
find_s(features, target)