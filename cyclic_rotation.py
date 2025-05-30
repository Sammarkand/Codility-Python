# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here

	# create an integer to store the array width
    width = len(A)

	# if the width of array is 0 or 1 nothing happens
	# if the the rotations(K) / width is remainder 0, also nothing needs to happen
	# you can not % by 0 so you need to include the first part
    if width < 2 or K % width == 0:
        # return it as you received it
        return A
	
	# if rotations(K) % width has a remainder and the width is < 2
    else:
		# create an array full of 0s at the appropiate width
        my_array = [0] * width
		# find the index(i) in width and iterate throught each position
        for i in range(width):
			# increment index K times and modulate width to find true index. Fill true index with A
            my_array [(i + K) % width] = A[i]
		#return the completed array
        return my_array