from Reci import *
import copy
import pickle

#ini
belt_capacity=60; #default mk1
resource_limit=belt_capacity; #usually is the case

#master_list is the main dictionary with 0s.
#print(master_list)


#desired output
#des_out=input("What do you want to make?")

#override
des_out="Iron Plate"
des_count=10


product=copy.deepcopy(master_list)
req_resource=copy.deepcopy(base_resource)


product[des_out][0]=des_count #input at iron plate a need of 10 production
# print("Start of Product")
# print(product)
# print("End of Product")


#---------------------------Working right here
product_size=len(product)
product_key=list(product.keys())

# print("Product Key",product_key)

count=0

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
        print("Factory b||", factory, product[x][1][factory],type(product[x][1][factory]))
        #---------------nid help here--------------------
        product[x][1][factory]+=1
        #---------------this one-------------------------
        #print(product)
        print("Factory a||", factory, product[x][1][factory],type(product[x][1][factory]))
        print("Product After||", x , product[x])
        
        #`y` is the key of output products. y="Iron Ingot"
        for y in temp_recipe["o"]: #materials made but backfed since we're trying to solve how much needed materials
            #print(temp_recipe["i"][y])
            product[y][0] -= temp_recipe["o"][y]
            #print(temp_product)
            im_prod_keys.add(y)
        for y in temp_recipe["i"]: #materials needed, y="Iron Ore"
            print("Required Input||",temp_recipe["i"])
            
            try:
                product[y][0] += temp_recipe["i"][y]
                im_prod_keys.add(y)
            except:
                print("It's a base resource!")
                req_resource[y] += temp_recipe["i"][y]
                im_base_keys.add(y)
            else:
                print("It's an intermediate resource!")
    
    else:
        checker[temp_index] = 0; #an operation did not happen in the loop
    
    if temp_product[0]<0:
        print("hmm, this is a negative")


        #this line needs a work also !!base resource is a different directory!!!
        for y in temp_recipe["o"]:
            if product[y][0] + temp_recipe["o"][y] < 0:
                print("needs a reverse!")
    
    
        
    count+=1;

final_product=dict()
final_base=dict()
print("Important Keys",im_prod_keys, im_base_keys)
for x in im_prod_keys:
    final_product[x] = product[x];
for x in im_base_keys:
    final_base[x] = req_resource[x];
print("Final Product",final_product)
print("Base Resource",final_base)