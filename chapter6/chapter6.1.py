""" write a function to count how many off numbers are in a list """
mylist= [0,2,3,7,11,12]

def count_odd(numlist):
    count=0
    
    for i in numlist:
        if i % 2  != 0:
            count+= 1
        
    return count

print(count_odd(mylist))

""" sum up al the even numbers in the list """

mylist= [0,2,3,7,11,12]

def sum_even(numlist):
    mysum=0
    
    for i in numlist:
        if i % 2 == 0:
            mysum=mysum+i
            
    return mysum

print(sum_even(mylist))

        
    