import pandas as pd
list1=[1,2,3,4,5]
series1=pd.Series(list1)
#this is the creation of the series data type using another list
print(series1)
# creating series by passing the list in the series it self & by index we can  change the  index as well
series2=pd.Series([10,28,30])
series5=pd.Series([10,28,30],index=['a','b','c'],dtype=float)
print(series2)
#EMPTY SERIES
series3=pd.Series([""])
print(series3)

# CREATING THE SERIES USING DICTIONARY
series4=pd.Series({'a':30,'b':28,'c':10})
print(series4)

#min_max_of_the_series
max_element= max(series4)
print("THE MAXIMUM ELEMENT OF THE SERIES4 IS:")
print(max_element)
print(min(series4))

# additon_of_the_series
print("THE SUM OF ALL THE SERIES IS;")
print(series1+series2)



