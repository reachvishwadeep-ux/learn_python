
"""
This is good case of recurrsion. We can use recursion to flatten the list. We can check if the element is a list or not. If it is a list, we can call the function recursively on that list. If it is not a list, we can add it to the result list.

"""

def recurrsive_function(item, flat_list):
    
    if(isinstance(item, list)):
        for each in item:
            recurrsive_function(each,flat_list)
    else:
        #print(item)
        flat_list.append(item)
        

my_list = [1,2,3, [4,5,[6,7,[9,10,11]]]]
flat_list = []
recurrsive_function(my_list, flat_list)
print(flat_list)