# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # Implement your solution here
	
	# br (binary rendering)
	# bin converts N to a binary string
	# [2:] removes the fist two chars "0b"
    br = str(bin(N))[2:]

	# We need two integers
	# one to keep tracks of the largest gap (number of 0s in any binary gap)
    largest = 0
	# another to keep track of how many 0s we've counted in the current gap
    zero_counter = 0

	# for loop that iterates through chars in "br" starting at the front
    for char in br:
	
		# if we catch a 1
        if char == '1':
			
			# if we're closing a gap and our last gap was bigger then we need to reset largest
            if largest < zero_counter:
                largest = zero_counter
			# any time you hit a 1 you are opening or closing and need to set the counter to zero
            zero_counter = 0
			
		# if we catch a 0
        else:
			# increment the counter
            zero_counter += 1
			
	# we don't need to worry about the 0s we counted in the else statement if they weren't in a true binary gap. largest won't increment unless we hit a 1 so it automatically ignores 0s tails.
	
	# return the largest gap we've found
    return largest