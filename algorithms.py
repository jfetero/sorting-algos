import random

class Algorithms():
	
	def __init__(self, arr):
		self.arr = arr








def bubble(arr):
	n = len(arr)

	for i in range(1, n):
		for j in range(n-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

	return arr

def insertion(arr):
	for i in range(1, len(arr)):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			arr[j], arr[j-1] = arr[j-1], arr[j]
			j -= 1
	
	return arr 

def binary_insertion(arr):

	def binary_search(arr, val, left, right):
		if left == right:
			if arr[left] < val:
				return left +1
			else:
				return left

		if left > right:
			return left

		while left <= right:
			mid = (left + right) // 2
			if val > arr[mid]:
				return binary_search(arr, val, mid+1, right)
			if val < arr[mid]:
				return binary_search(arr[:mid], val, left, mid-1)
			else:
				return mid

	for i in range(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr [:j] + [val] + arr[j:i] + arr[i+1:]

	return arr


def quick(arr):
	def util(arr,low,high): 
		left = low-1          
		pivot = arr[high]     

		for j in range(low , high):  
			if arr[j] < pivot:
				left += 1 
				arr[left],arr[j] = arr[j],arr[left] 

		arr[left+1],arr[high] = arr[high],arr[left+1] 
		return left+1
	  
	
	def quick_util(arr,low,high): 
		if low < high: 
			pivot = util(arr,low,high)  
			quick_util(arr, low, pivot-1) 
			quick_util(arr, pivot+1, high)

		return arr

	low = 0
	high = len(arr)-1
	return quick_util(arr,low,high)



def merge(arr):

	def util(arr):
		if len(arr) == 1:
			return arr

		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]

		left = util(left)
		right = util(right)

		ret = []

		i = 0
		j = 0
		while len(left[i:]) > 0 and len(right[j:]) > 0:
			if left[i] > right[j]:
				ret.append(right[j])
				j +=1
			else:
				ret.append(left[i])
				i+=1

		while len(left[i:]) > 0:
			ret.append(left[i])
			i +=1 

		while len(right[j:]) > 0:
			ret.append(right[j])
			j +=1

		return ret

	return util(arr)


def heap(arr):

	def heapify(arr, idx=0):
		i = idx
		while True:
			l = i *2 +1
			r = i *2 +2
			mx = i
			if l < len(arr) and arr[i]<  arr[l]:
				mx = l
			if r < len(arr) and arr[mx] < arr[r]:
				mx = r
			if mx == i:
				break
			else:
				arr[i], arr[mx] = arr[mx], arr[i]
				i = mx
		return arr


	arr = heapify(arr)
	ret = []
	while arr:
		temp = arr[0]
		arr[0] = arr[len(arr)-1]
		del arr[len(arr)-1]
		arr = heapify(arr)
		ret.append(temp)

	return ret[::-1] 




def radix(arr):
	num = len(str(max(arr)))

	for digit in range(num):
		bucket = [[] for i in range(10)]
		for x in arr:
			idx = x // 10 ** digit % 10
			bucket[idx].append(x)
		arr = []
		for t in bucket:
			arr.extend(t)
	return arr


 








	


arr = [random.randint(0,100000000) for x in range(1_000_000)]
#print(arr)
print(radix(arr))


