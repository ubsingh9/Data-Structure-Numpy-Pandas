def frequent_element(my_list):
    frequency={}
    for item in my_list:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1

    max_count=0
    value=None
    for element in frequency:
        if frequency[element]>max_count:
            max_count=frequency[element]
            value=element

    return(value, max_count)
    




my_list =[1,2,3,4,1,2,6,1,2,4,1,9]
most_frequent=frequent_element(my_list)
print(most_frequent)  


