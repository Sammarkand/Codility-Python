# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here

    #always try to solve algebraically first. It's so much cheaper

    #calculate how long the array should be if it weren't missing an element
    expected_length = len(A) + 1

    #sum all of the elements in the given array
    sum_A = sum(A)

    #calculate what the sum should be of the array if it weren't missing an element. 
    #this only works if you know where the array starts (in this case 1)
    expected_sum = expected_length * (expected_length + 1) // 2

    #find and return the missing element by subtracting the sum of the given array from the expected sum
    return expected_sum - sum_A
