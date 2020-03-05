import numpy as np

# Class excersice 1 (se 04 Numpy)
ex = np.arange(10,30).reshape(4,5)

yellow = ex[0,0] # 0 = 0de array og nulte element
blue = ex[:,1::2] # : = se på y-aksen, 1: = start fra 1, :2 = hver andet element
green = ex[0:3,2:3] # Vil se de første tre elementer fra y aksen på tredje plads
red = ex[0, 1:4]
dark_blue = ex[::2, 4] # ::2 -> Hver anden fra y-aksen på fjerde element

# Class excersice 2
# 1. Slice out 12 13 14 from the above cube using only one slice. e.g: a:,:,:
# 2. Slice out 3 12 21.
# 3. Slice out all y-values where x is 2 and z is 0.

a = np.arange(0, 27).reshape((3, 3, 3)) # = (z, y, x)

a1 = a[1,1,:] 
a2 = a[:, 1, 0]
a3 = a[0, :, 2]


# Class excersice 3 
data = np.arange(1, 101).reshape(10,10)
print(data)
#1
mask1 = data % 2 == 0
#print(data[mask1])

#2
where2 = np.where(data % 10 == 6)
print(where2) # Giver indices where condition is true
print(data[where2]) # Gives the actual data

#3
mask3 = (data == 8) | (data % 3 == 0) | (data//10 == 8)
print(data[mask3])


"""
--------------------------------- Class excersice 4 ---------------------------------
"""
# 1. Load befkbhalderstatkode.csv into numpy array (File cannot be found)
filename = './befkbhalderstatkode.csv'
bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

# 2. How many german children were 0 years in 2015
# Checking that year is 2015, stat code is 5180 (Germany) and age = 0
mask = (bef_stats_df[:,0] == 2015) & (bef_stats_df[:,3] == 5180) & (bef_stats_df[:,2] == 0)

# Summing up the colon that contains number of given condition
bef_stats_df[mask][:,4].sum()

# 3 Create a function that can take any combination of the 4 parameters (AAR, BYDEL, 
#   ALDER, STATKODE) and return population data (Works - test in 04 Numpy)

def get_population_data(year, city, age, statecode):
    mask1 = (bef_stats_df[:,0] == year) & (bef_stats_df[:,3] == statecode) & (bef_stats_df[:,2] == age) & (bef_stats_df[:,1] == city)
    return bef_stats_df[mask1]

print(get_population_data(2000, 1, 5, 5100))

# 4 Create a new function that can provide sum of all ages if age is not provided
def get_sum_of_people(year, city, statecode, age=None,):
    if(age is None):
        mask = (bef_stats_df[:,0] == year) & (bef_stats_df[:,3] == statecode) & (bef_stats_df[:,1] == city)
        return bef_stats_df[mask][:,4].sum()
    else:
        mask = (bef_stats_df[:,0] == year) & (bef_stats_df[:,3] == statecode) & (bef_stats_df[:,2] == age) & (bef_stats_df[:,1] == city)
        return bef_stats_df[mask]

def get_avg_no_of_citizens():
    pass




