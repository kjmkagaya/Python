


"""

Sorting Algorithm
sort_values() provides a provision to choose the algorithm from mergesort, heapsort and quicksort. Mergesort is the only stable algorithm.


"""


import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')

print (sorted_df)


"""

Its output is as follows −

  col1 col2
1    1    3
2    1    2
3    1    4
0    2    1



"""
