from Reci import *
import copy
import pickle

#ini
belt_capacity=60; #default mk1
resource_limit=belt_capacity; #usually is the case

#master_list is the main dictionary with 0s.
#print(master_list)


#desired output
des_out=input("What do you want to make?")

#override
des_out="Iron Plate"
des_count=10


product=copy.deepcopy(master_list)
print(product)



