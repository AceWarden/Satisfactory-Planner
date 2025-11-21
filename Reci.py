import pickle
import copy

sample_dat_1=[
    {#Recipe 0
            "i": {},
            "o": {},
            "f": "",
        },
],


#dat{desired_output}[recipe#]{i/o'/f}{material}=#
#global dat
dat={
    "Iron Ingot":[
        {#Recipe 0 Smelter
            "i": {"Iron Ore":30},
            "o": {"Iron Ingot":30},
            "f": "Smelter"
        },
        {#Recipe 1
            "i": {},
            "o": {},
            "f": ""
        },
    ],
    
    
    "Copper Ingot":[
        {#Recipe 0 Smelter
            "i": {"Copper Ore":30},
            "o": {"Copper Ingot":30},
            "f": "Smelter"
        },
        {#Recipe 1
            "i": {},
            "o": {},
            "f": "",
        },
    ],
    
    
    "Iron Plate":[
        {#Recipe 0 Constructor
            "i": {"Iron Ingot":30},
            "o": {"Iron Plate":20},
            "f": "Constructor"
        },    
    ],
    
    
    "Iron Rod":[
        {#Recipe 0 Constructor
            "i": {"Iron Ingot":15},
            "o": {"Iron Rod":15},
            "f": "Constructor"
        },
    ],
    
    
    "Screws":[
        {#Recipe 0 Constructor
            "i": {"Iron Rod":10},
            "o": {"Screws":40},
            "f": "Constructor"
        },
    ],


    "Copper Sheet":[
        {#Recipe 0 Constructor
            "i": {"Copper Ingot":20},
            "o": {"Copper Sheet":10},
            "f": "Constructor"
        },
    ],
    
    
    "Steel Ingot":[
        {#Recipe 0 Foundry
            "i": {"Iron Ore":45, "Coal":45},
            "o": {"Steel Ingot":45},
            "f": "Foundry"
        },
        {#Recipe 1 Foundry
            "i": {"Iron Ingot":40, "Coal":40},
            "o": {"Steel Ingot":60},
            "f": "Foundry"
        },
    ],
    
    
    "Steel Beam":[
        {#Recipe 0 Constructor
            "i": {"Steel Ingot":60},
            "o": {"Steel Beam":15},
            "f": "Constructor"
        },
    ],
    
    
    "Steel Pipe":[
        {#Recipe 0 Constructor
            "i": {"Steel Ingot":30},
            "o": {"Steel Pipe":20},
            "f": "Constructor"
        },
    ],
    
    
    "Wire":[
        {#Recipe 0 Constructor
            "i": {"Copper Ingot":15},
            "o": {"Wire":30},
            "f": "Constructor"
        },
        {#Recipe 0 Constructor
            "i": {"Caterium":15},
            "o": {"Wire":120},
            "f": "Constructor"
        },
    ],
    
    
    "Cable":[
        {#Recipe 0 Constructor
            "i": {"Wire":60},
            "o": {"Cable":30},
            "f": "Constructor"
        },
    ],
    
    
    "Reanimated SAM":[
        {#Recipe 0 Constructor
            "i": {"SAM":120},
            "o": {"Reanimated SAM":30},
            "f": "Constructor"
        },
    ],
    
    
    "Concrete":[
        {#Recipe 0 Constructor
            "i": {"Limestone":45},
            "o": {"Concrete":15},
            "f": "Constructor"
        },
    ],
    
    
    "Raw Quartz":[
        {#Recipe 0 Constructor
            "i": {"Raw Quartz":37.5},
            "o": {"Quartz Crystal":22.5},
            "f": "Constructor"
        },
    ],
    
    
    "Silica":[
        {#Recipe 0 Constructor
            "i": {"Raw Quartz":22.5},
            "o": {"Silica":37.5},
            "f": "Constructor"
        },
    ],
    
    
    "Reinforced Iron Plate":[
        {#Recipe 0 Assembler
            "i": {"Iron Plate":30, "Screws":60},
            "o": {"Reinforced Iron Plate":5},
            "f": "Assembler"
        },
    ],
    
    
    "Modular Frame":[
        {#Recipe 0 Assembler
            "i": {"Reinforced Iron Plate":3, "Iron Rod":12},
            "o": {"Modular Frame":2},
            "f": "Assembler"
        },
    ],
    
    
    "Encased Industrial Beam":[
        {#Recipe 0 Assembler
            "i": {"Steel Beam":18, "Concrete":36},
            "o": {"Encased Industrial Beam":6},
            "f": "Assembler"
        },
        {#Recipe 1
            "i": {"Steel Pipe":24, "Concrete":20},
            "o": {"Encased Industrial Beam":4},
            "f": "Assembler",
        },
        
    ],
    
    
    "Rotor":[
        {#Recipe 0
            "i": {"Iron Rod":20, "Screws":100},
            "o": {"Rotor":4},
            "f": "Assembler",
        },
    ],
    
    
    "Stator":[
        {#Recipe 0
            "i": {"Steel Pipe":15, "Wire":40},
            "o": {"Stator":5},
            "f": "Assembler",
        },
    ],
    
    
    "Motor":[
        {#Recipe 0
            "i": {"Rotor":10, "Stator":10},
            "o": {"Motor":5},
            "f": "Assembler",
        },
    ],
    
    
    "Black Powder":[
        {#Recipe 0
            "i": {"Coal":15, "Sulfur":15},
            "o": {"Black Powder":30},
            "f": "Assembler",
        },
    ],
    
    
    
};

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#print(len(dat))
#for x in dat:
    #print(x)
    #print(type(x))
    #temp=dat[x]
    #print(temp[0])
    #print(temp[0]["f"])
    #print(temp[0]["i"])
    #print(temp[0]["o"])

factory_list={}
for x in dat:
    temp_reci=dat[x]    #[{"i":{mat:#},...,},[...]] These are the recipes available for 1 material
    #print(temp_reci)
    for y in temp_reci:
        temp_fact=y["f"]
        #print(temp_fact)
        #print(type(temp_fact))
        if temp_fact not in factory_list and temp_fact!="":
            factory_list.update({temp_fact:0});#print(x)
#print(factory_list)

#global master_list
master_list={}
count=0;
for x in dat:
    master_list.update({x:[0,0]})#factory_list]})
    count+=1

#master_list={material: [required ppm, {factory_type:# of factory, factory_type:# of factory}],...,}


#print(master_list)
#print(count)



base_resource={
"Iron Ore":0, 
"Copper Ore":0,
"Limestone":0,
"Caterium Ore":0,
"Raw Quartz":0,
"Sulfur":0,
"Coal":0,
"SAM":0,
"Water":0,
};


#Default Recipe Setup
#dat{desired_output}[recipe#]{i/o'/f}{material}=#
default=copy.deepcopy(dat);

for x in default:   #looping through the strings of desired output
    default[x]=default[x][0]    #pick the 1st recipe always
#print(default)


try:
    with open('user_recipe.txt','rb') as file:
        user_recipe=pickle.load(file)
        file.close()
except:
    with open('user_recipe.txt','wb') as file:
        pickle.dump(default,file)
        user_recipe=default
        file.close()
#print(user_pref)
#print(user_pref["Iron Ingot"]["i"]["Iron Ore"])