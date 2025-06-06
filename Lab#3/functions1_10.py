def unique_elements(lst):
    unique_list = []  
    for num in lst:
        if num not in unique_list:  
            unique_list.append(num)
    return unique_list  

nums = list(map(int, input("eEnter num : ").split()))

print("Unique elements:", unique_elements(nums))