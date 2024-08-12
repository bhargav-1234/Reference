#1. Python program to interchange first and last elements in a list

# Input : [12, 35, 9, 56, 24] Output : [24, 35, 9, 56, 12] Input : [1, 2, 3] Output : [3, 2, 1]

# swap function
def swapList(newlist):
    size= len(newlist)

    #swaping
    temp =newlist[0]
    newlist[0]= newlist[size-1]
    newlist[size-1]=temp

    return newlist

# driver code
newlist =[12,35,9,56,24]
print(swapList(newlist))
