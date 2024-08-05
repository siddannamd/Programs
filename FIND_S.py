import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\sidda\Desktop\6th sem\Machine Learning Programs\enjoySport.csv')
data
attribute = np.array(data)[:,:-1]
attribute
target = np.array(data)[:,-1]
target

def train(att, tar):
    specific_h = None
    for i, val in enumerate(tar):
        if val == 'yes':
            specific_h = att[i].copy()
            break

    if specific_h is None:
        raise ValueError("No positive examples (i.e., 'yes' values) in the target array.")

    for i, val in enumerate(att):
        if tar[i] == 'yes':
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
    return specific_h

print(train(attribute, target))
