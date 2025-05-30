# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here

    #create int length of array A for iterative purposes
    length = len(A)
    #create empty array to append and remove from
    my_array = []
    
    #check every element in array individually
    for i in range(length):
        #if element exists in my_array than I have found the pair. remove that element from my_array.
        if A[i] in my_array:
            my_array.remove(A[i])
        #else element's pair has not been found. Append to my array.
        else:
            my_array.append(A[i])
    #All pairs will have removed and only one element will not have. Return last remaining element.
    return my_array[0]

