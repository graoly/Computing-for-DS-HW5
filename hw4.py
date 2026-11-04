##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
from functools import reduce
import pandas as pd
from datetime import date
from geopy import distance

string_text = ["Simba and Nala are lions.", "I laugh in the face of danger.",
 "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 

#def add(x,y):
#    return x+y

def count_simba(input_string):
    simba_counts = map(lambda x: x.count("Simba"), input_string)
    #final_count = reduce(add,simba_counts, 0)
    final_count = reduce(lambda x,y : x+y,simba_counts, 0)
    return final_count

print(count_simba(string_text))

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

date_1 = [date(2026,10,2),date(2026,10,5),date(2026,10,11)]

def get_day_month_year(date_list):
    date_reduce = map(lambda x: (x.day, x.month, x.year), date_list)
    rows = reduce(lambda start, item: start + [item], date_reduce, [])
    df = pd.DataFrame(rows, columns = ['day','month','year'])
    return df

print(get_day_month_year(date_1))

# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

lat_long = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
def compute_distance(lat_long_list):
    distances = map(lambda pair: distance.distance(pair[0],pair[1]).km, lat_long_list)
    final_distance_list = reduce(lambda start, d: start + [d], distances,[])
    return final_distance_list

print(compute_distance(lat_long))

# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

def sum_general_int_list(lst: list) -> int:
  
    flat_list = map(lambda element: sum_general_int_list(element) if isinstance(element, list) else element, lst)
    reduced_sum = reduce(lambda x, y: x + y, flat_list, 0)
    return reduced_sum
    
# Tests below, uncomment # to view function working
# a = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
# print(sum_general_int_list(a))
# print("Number above should be the integer 48")
# b = [[2], 3, [[1,2],5]]
# print(sum_general_int_list(b))
# print("Number above should be the integer 13")