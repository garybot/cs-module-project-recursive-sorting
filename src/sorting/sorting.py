# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
	elements = len(arrA) + len(arrB)
	merged_arr = [0] * elements

	# Your code here
	ai = 0
	bi = 0
	while (ai + bi < elements):
		if ai >= len(arrA):
			merged_arr[ai + bi] = arrB[bi]
			bi += 1
		elif bi >= len(arrB):
			merged_arr[ai + bi] = arrA[ai]
			ai += 1
		elif arrA[ai] < arrB[bi]:
			merged_arr[ai + bi] = arrA[ai]
			ai += 1
		elif arrA[ai] >= arrB[bi]:
			merged_arr[ai + bi] = arrB[bi]
			bi += 1
	return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
	# Base
	if len(arr) <= 1:
		return arr;

	# Recursive
	else:
		# divide into lhs, rhs
		LHS = merge_sort(arr[0:len(arr)//2])
		RHS = merge_sort(arr[len(arr)//2:len(arr)])
		arr = merge(LHS, RHS)

	return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
	# Your code here


# def merge_sort_in_place(arr, l, r):
	# Your code here

