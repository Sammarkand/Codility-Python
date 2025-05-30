# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here

    #import math to use the ciel function which gives the solution when a whole number or rounds up on a decimal
    import math

    #don't jump if the frog is already where he wants to be
    if X == Y:
        return 0
    #if the starting position plus one jump is greater than or equal to the destination then only jump once
    elif Y <= (X + D):
        return 1

    #otherwise divide difference of start and finish by jumps and round up
    else:
        return math.ceil((Y - X) / D)
