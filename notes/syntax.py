# joining tables with numpy dataframe 
import numpy as np 

df1 = pd.DataFrame({
    'A': ['Alice', 'Bob', 'Charlie'],
    'B': ['New York', 'Chicago', 'Los Angeles']
})

df2 = pd.DataFrame({
    'C': ['Laptop', 'Phone', 'Tablet'],
    'D': [1000, 800, 600]
})

np.merge(df1, df2)

# joining tables in datascience UCB 
# https://www.data8.org/datascience/tutorial.html

from datascience import Table
import matplotlib
matplotlib.use('Agg')
from datascience import Table
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')

t = Table().with_columns(
    'letter', ['a', 'b', 'c', 'z'],
    'count',  [  9,   3,   3,   1],
    'points', [  1,   2,   2,  10],
)

t2 = Table().with_columns(
    'letter', ['d', 'e', 'f', 'g'],
    'count',  [  10,   4,   5,   6],
    'points', [  12,   23,   24,  11],
)

new_table = t.join("letter", t2, "letter")

## Using Select Method from a table to display the certain columns you choose 

yelp_google_tbl = new_table.select("Yelp", "Google")


## Group Method

cones = Table().with_columns(
    'Flavor', make_array('strawberry', 'chocolate', 'chocolate', 'strawberry', 'chocolate'),
    'Price', make_array(3.55, 4.75, 6.55, 5.25, 5.25)
)
cones

cones.group('Flavor') # counts the number of same flavors in a column 


# Using group 
## How Group Works: it collects values into an array and then applies a function to that array. 

california_burritos = burritos.where("Menu_Item", are.containing("California")).select("Menu_Item", "Overall").group("Menu_Item", np.average)


# Indexing table for highest value
table.column("Menu_Item").item(0)

# Histogram with edges of bins 
cost_bins = np.arange(0, 15, 1)
sd_burritos = burritos_table.where("Name", "San Diego") 
sd_burritos = burritos_table.hist("Cost", bins=cost_bins)


