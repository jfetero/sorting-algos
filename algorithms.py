import random
import heapq as h
import time



def bubble(arr, drawList, speed):
	n = len(arr)

	for i in range(1, n):
		for j in range(n-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				drawList(arr,['red' if x == j or x == j+1 else 'sky blue' for x in range(int(len(arr)))])
				time.sleep(speed)

	drawList(arr,['SeaGreen3' for _ in range(int(len(arr)))])


def insertion(arr,drawList):
	for i in range(1, len(arr)):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			arr[j], arr[j-1] = arr[j-1], arr[j]
			j -= 1
			drawList(arr)
			time.sleep(.2)
	
	return arr 

def binary_insertion(arr, drawList):

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

	drawList(arr)
	time.sleep(.2)

	return arr


def quick(arr, drawList, speed):
	def util(arr,low,high): 
		left = low-1          
		pivot = arr[high]    

		drawList(arr, get_color(int(len(arr)), low, high, left, left)) 
		time.sleep(speed)

		for j in range(low , high):  
			if arr[j] < pivot:
				drawList(arr, get_color(int(len(arr)), low, high, left, j, swap = True))
				time.sleep(speed)

				left += 1 
				arr[left],arr[j] = arr[j],arr[left] 
			drawList(arr, get_color(int(len(arr)), low, high, left, j))
			time.sleep(speed)

		arr[left+1],arr[high] = arr[high],arr[left+1] 
		drawList(arr, get_color(int(len(arr)), low, high, left, left + 1, swap = True))
		time.sleep(speed)
		return left+1
	  
	
	def quick_util(arr,low,high, speed): 
		if low < high: 
			pivot = util(arr,low,high)  
			quick_util(arr, low, pivot-1, speed) 
			quick_util(arr, pivot+1, high, speed)

		drawList(arr,['SeaGreen3' for _ in range(int(len(arr)))]) 
		return arr


	def get_color(length, low, high, wall, idx, swap = False):
		colors = []
		for i in range(length):
			if i >= low and i <= high:
				colors.append('sky blue')
			else:
				colors.append('red')

			if i == high:
				colors[i] = 'blue'
			elif i == wall:
				colors[i] = 'sky blue'
			elif i == idx:
				colors[i] = 'yellow2'
			if swap:
				if i == wall or i == idx:

					colors[i] = 'SeaGreen3'

		return colors


	low = 0
	high = len(arr)-1
	return quick_util(arr,low,high, speed)



def merge_sort(arr, drawList):
	if len(arr) <= 1:
		return arr

	mid = len(arr)//2
	left = arr[:mid]
	right = arr[mid:]

	left = merge_sort(left, drawList)
	right = merge_sort(right,drawList)

	ret = []
	i = j = 0
	
	while len(left[i:]) > 0 and len(right[j:]) > 0:
		if left[i] > right[j]:
			ret.append(right[j])
			j +=1
		else:
			ret.append(left[i])
			i+=1
	if len(left) >0:
		ret.extend(left[i:])
	if len(right) > 0:
		ret.extend(right[j:])

	drawList(ret)
	time.sleep(.2)

	return ret


def heap(arr, drawList):
	ret = []
	h.heapify(arr)
	for _ in range(len(arr)):
		ret.append(h.heappop(arr))
	drawList(ret)
	time.sleep(.2)

	return ret


def radix(arr, drawList):
	num = len(str(max(arr)))

	for digit in range(num):
		bucket = [[] for i in range(10)]
		for x in arr:
			idx = x // 10 ** digit % 10
			bucket[int(idx)].append(x)
			drawList(arr)
			time.sleep(.2)
		arr = []
		for t in bucket:
			arr.extend(t)


	return arr

def counting(arr, drawList):
	mx = max(arr)	
	temp = [0 for _ in range(int(mx+1))]
	ret = []

	for x in arr:
		temp[int(x)] +=1

	for i in range(len(temp)):
		if temp[int(i)] != 0:
			ret += [i for _ in range(int(temp[i]))]

	drawList(ret)
	time.sleep(.2)
	return ret

 








	

if __name__ == '__main__':
	#arr = [random.randint(0,50_000) for x in range(10_000)]
	#arr1 = [random.randint(0,10000) for x in range(10_000)]
	data = [9,8,11,7,6,5,10,4,3,2,12,1]

	print(data)
	print(radix(data))


