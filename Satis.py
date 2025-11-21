from Reci import *
import copy
import pickle


#master_list is the main dictionary with 0s.
#print(master_list)


#desired output
#des_out=input("What do you want to make?")
#----------------------------- Input v1 ----------------------------------
#override
des_out="Iron Plate"
des_count=10

#------------------------------ Input v2 ---------------------------------
des_out = "Iron Plate"  #desired output
btl_nk = "Iron Ore"     #bottleneck
belt_cap = 60;          #default mk1


#-------------------------------------------------------------------------
des_count = 1          #default to run code. Not an input



#master_list={material: [required ppm, {factory_type:# of factory, factory_type:# of factory}],...,}
product = copy.deepcopy(master_list)
req_resource = copy.deepcopy(base_resource)


product[des_out][0] = des_count #input at iron plate a need of 10 production
# print("Start of Product")
# print(product)
# print("End of Product")


#--------------------------- Working right here -------------------------
product_size = len(product)
product_key = list(product.keys())

# print("Product Key",product_key)

count = 0

print("Length of Product ", product_size)

checker = [1] * product_size;
im_prod_keys=set();
im_base_keys=set();


while checker != [0] * product_size: # x in product:
    temp_index = count % product_size
    x = product_key[temp_index] #to keep consistent from old code
    temp_product = product[x] #Check here?
    print(temp_index)
    #print("Product Check per Key ||", x, product[x])
    
    
    if temp_index == product_size - 1:
        checker = [1] * product_size;
    
    # if count == 0:
        # print("Product [x]", x, product[x])
        # print(temp_product)
        # print("User Recipe for [X]")
        # print(user_recipe[x])
        # print("")
    if temp_product[0]>0:
        print("Product Before||", x , product[x])
        temp_recipe = user_recipe[x]
        print("Temp_Recipe||", x, temp_recipe)
        factory = temp_recipe["f"]
        print(factory, type(factory))
#------------------------------- Proportion -------------------------------------------        
        #finding the proportion for the entire system
        #x is the name of the main material
        
        #print("Recipe for input in question",x,temp_recipe["o"][x])
        proportion=temp_product[0]/temp_recipe["o"][x]
        print(proportion)
        
#--------------------------------------------------------------------------        
        #`y` is the key of output products. y="Iron Ingot"
        for y in temp_recipe["o"]: #materials made but backfed since we're trying to solve how much needed materials
            #print(temp_recipe["i"][y])
            
            product[y][0] -= temp_recipe["o"][y] * proportion
            #print(temp_product)
            im_prod_keys.add(y)
        for y in temp_recipe["i"]: #materials needed, y="Iron Ore"
            print("Required Input||",temp_recipe["i"])
            
            try:
                product[y][0] += temp_recipe["i"][y] * proportion
                im_prod_keys.add(y)
            except:
                print("It's a base resource!")
                req_resource[y] += temp_recipe["i"][y] * proportion
                im_base_keys.add(y)
            else:
                print("It's an intermediate resource!")
        print("Factory b||", factory, product[x][1],type(product[x][1]))
        #---------------nid help here--------------------
        product[x][1] = proportion
        #---------------this one-------------------------
        #print(product)
        #print("Factory a||", factory, product[x][1],type(product[x][1]))
        print("Product After||", x , product[x])
    else:
        checker[temp_index] = 0; #an operation did not happen in the loop
    
    if temp_product[0]<0:
        print("hmm, this is a negative")


        #this line needs a work also !!base resource is a different directory!!!
        for y in temp_recipe["o"]:
            if product[y][0] + temp_recipe["o"][y] < 0:
                print("needs a reverse!")
    
    
        
    count+=1;

print(product)

final_product=dict()
final_base=dict()
print("Important Keys",im_prod_keys, im_base_keys)
for x in im_prod_keys:
    final_product[x] = product[x];
for x in im_base_keys:
    final_base[x] = req_resource[x];
print("Final Product",final_product)
print("Base Resource",final_base)


#-------------------- Reverse Proportion -----------------------

list_wrt_base=[0]*len(final_base)
count=0;

for x in final_base:
    curr_prop = belt_cap / final_base[x]    #proportion wrt belt speed
    print(curr_prop)
    temp_prod=copy.deepcopy(final_product)
    temp_base=copy.deepcopy(final_base)
    
    for y in temp_prod:   #The [0] becomes the ppm information in this loop
        temp_prod[y][1] *= curr_prop
        temp_prod[y][0] = user_recipe[y]["o"][y] * temp_prod[y][1]
        
    
    for y in temp_base:
        temp_base[y] *= curr_prop
        
        
        
    
    
    
    list_wrt_base[count] = [temp_prod,temp_base]
    count+=1;

print("current proportionality", list_wrt_base)