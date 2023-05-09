
if __name__ == '__main__':
    #Creating a list
    l = [1, 2, 3, 4]

    print(l) # 1 2 3 4 

    #Accessing items in a list using indexing    
    print(l[0])   # Output: 1
    print(l[2])   # Output: 3

    #Slicing a list to extract a sublist:   
    sub_list = l[1:3]
    print(sub_list)     # Output: [2, 3]

    #Modifying an item in a list: 
    l[2] = 10
    print(l)      # Output: [1, 2, 10, 4]

    #Adding an item to the end of a list:
    l.append(5)
    print(l)      # Output: [1, 2, 10, 4, 5]

    #Removing an item from a list:    
    l.remove(2)
    print(l)      # Output: [1, 10, 4, 5]

    #Iterating over a list using a for loop:
    for val in l:
        print(val) # 1  10 4 5

    #Iterating over a list using a for loop with index:
    for i in range(len(l)):
        print(l[i]) # 1  10 4 5


    #Insert in a list
    l.insert(2, 100) #index = 2 , value = 10

    print(l) # [1 , 10, 100, 4, 5]


    #pop last elemnet 
    l.pop() 

    print(l) #[ 1, 10, 100, 4]


    del l[2]      # remove the element at index 2
    print(l)      # Output: [1, 10, 4]


    l.pop(2) # remove the element at index 2
    print(l)  #Output : [1, 10]

