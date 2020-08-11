# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
	mid = (start + end) // 2
	if mid < 0:
		return -1
	elif arr[mid] == target:
		return mid;
	elif arr[mid] < target:
		return binary_search(arr, target, mid + 1, end)
	else:
		return binary_search(arr, target, start, mid)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
	min = 0
	max = len(arr)
	while (max - min):
		i = (min + max) // 2
		if arr[i] == target:
			return i
		elif target < arr[i]:
			if arr[1] > arr[0]:
				max = i
			else:
				min = i + 1
		else:
			if arr[1] > arr[0]:
				min = i + 1
			else: 
				max = i
	return -1
