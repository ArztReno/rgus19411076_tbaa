# date : 20/12/2020
# Author : Renato Gusani
# Student no. : x19411076
# Question 4 – Linear and Associative Data Structures : a2, b2, c2, d2

# * * * * * * * * * * question a.2) * * * * * * * * * *

import queue

# these are my seqeunces to house all the car details
cars_parked = [1, 2, 3, 4, 5, 6, 7, 8]
registration_number = ["11AA", "22BB", "33CC", "44DD", "55EE", "66FF", "77GG", "88HH"]
make = ["nissan", "opel", "tesla", "volkswagen", "porsche", "bugatti", "bmw", "bezo"]
model = [1, 2, 3, 4, 5, 6, 7, 8]
colour = ["red", "green", "blue", "organge", "white", "silver", "black", "purple"]
nct_expire = [2001, 2003, 2004, 2005, 2006, 2007, 2008]

# this is my queue stack
cars_parked = queue.Queue(5) # Setting the max size to 5.
cars_parked.put(1)
cars_parked.put(2)
cars_parked.put(3)
cars_parked.put(4)
cars_parked.put(5)
cars_parked.put(6)
cars_parked.put(7)
cars_parked.put(8)
print(cars_parked.full()) # will return true.
block = False
#cars_parked.put(6, block)
print("size", cars_parked.qsize())
while not cars_parked.empty():
print (cars_parked.get()) # 1 2 3 4 5 6 7 8


# * * * * * * * * * * question b.2) * * * * * * * * * *


# Question
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

#Answer
print(sampleDict['class']['student']['marks']['history'])


# * * * * * * * * * * question c.2) * * * * * * * * * *


set1 = {100,200,300,400,500}
set2 = {400,500,600,700,800}
print("Original sets:")
print(set1)
print(set2)
print("Removing the intersection of a 1st set from the 1st set using difference_update():")
set1.difference_update(set1)
print(set1)
print(set2)


# * * * * * * * * * * question d.2) * * * * * * * * * *


def CountFrequency(my_list): 
      
   # Creating an empty dictionary  
   count = {} 
   for i in [100, 100, 100, 500, 500, 300, 100, 300, 300, 100 ,400, 400, 400, 200, 200, 200, 200]: 
    count[i] = count.get(i, 0) + 1
   return count 
  
# Driver function 
if __name__ == "__main__":  
    my_list =[100, 100, 100, 500, 500, 300, 100, 300, 300, 100, 400, 400, 400, 200, 200, 200, 200] 
    print(CountFrequency(my_list)) 