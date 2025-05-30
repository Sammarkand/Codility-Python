# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    #start by creating a constant for the sum of the given array so you don't have to recalculate it all the time
    total_sum = sum(A)
    #initialize the left sum which will change as we iterate through the array
    left_sum = 0
    #initialize a variable to store the smallest difference found so far
    min_diff = float('inf')

    #iterate through the array but remember you are splitting which means you have -1 positions to work with
    for i in range(len(A)-1):
        #add the new number left of the split to the left sum
        left_sum += A[i]
        #subtract the left sum from the total sum to find the current right sum
        right_sum = total_sum - left_sum
        #find the absolute value of the difference. It doesn't matter which order the sums are in
        diff = abs(left_sum - right_sum)
        #update the minimum difference if the difference in this iteration is smaller
        min_diff = min(min_diff, diff)

    #return the smallest difference you've found
    return min_diff
