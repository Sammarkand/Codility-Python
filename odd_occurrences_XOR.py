# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    #initialize an int at 0 so that you don't cancel out anything by accident 
    num = 0

    #iterate through the array
    for i in range(len(A)):
        #apply the XOR operator to add unique bits and remove matching bits 
        num = num ^ A[i]

    #unique bits are returned in hexadecimal     
    return num
