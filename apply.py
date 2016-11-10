import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

# Change False to True for this block of code to see what it does

# DataFrame apply() - use case 2
if False:
    print df.apply(np.mean)
    print df.apply(np.max)


def sl_1D(c):
    return np.sort(c)[-2]


def second_largest(df):
    '''
    Fill in this function to return the second-largest value of each 
    column of the input DataFrame.
    '''
    # return df.sort_index()
    return df.apply(sl_1D)

print second_largest(df)
