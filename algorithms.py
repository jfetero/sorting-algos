import random
import heapq as h
import time


#=========================== Bubble Sort ===================================
def bubble(arr, drawList, speed):
	n = len(arr)

	for i in range(1, n):
		for j in range(n-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				drawList(arr,['red' if x == j or x == j+1 else 'sky blue' for x in range(len(arr))])
				time.sleep(speed)

	drawList(arr,['SeaGreen3' for _ in range(len(arr))])

#=========================== Insetion Sort =====================================
def insertion(arr,drawList, speed):
	for i in range(1, len(arr)):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			arr[j], arr[j-1] = arr[j-1], arr[j]
			j -= 1
			drawList(arr,['red' if x ==j or x == j-1 else 'blue' if x == i else 'sky blue'  for x in range(len(arr))])
			time.sleep(speed)
	drawList(arr,['SeaGreen3' for _ in range(len(arr))])
	
	return arr 

#============================ Binary-Insertion Sort ==============================
def binary_insertion(arr, drawList, speed):

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

		drawList(arr,['gold' if x <= i else 'blue' if x == i else 'sky blue' for x in range(len(arr))])
		time.sleep(speed)

		j = binary_search(arr, val, 0, i-1)

		drawList(arr,['blue' if x== i  else 'red' if x == j else 'gold' if x < i else 'sky blue' for x in range(len(arr))])
		time.sleep(speed)

		arr = arr [:j] + [val] + arr[j:i] + arr[i+1:]
		
	drawList(arr,['SeaGreen3' for _ in range(len(arr))]) 
	return arr


#============================= Quick Sort ======================================
def quick(arr, drawList, speed):
	def util(arr,low,high): 
		left = low-1          
		pivot = arr[high]    

		drawList(arr, color(len(arr), low, high, left, left)) 
		time.sleep(speed)

		for j in range(low , high):  
			if arr[j] < pivot:

				drawList(arr, color(len(arr), low, high, left, j, swap = True))
				time.sleep(speed)

				left += 1 
				arr[left],arr[j] = arr[j],arr[left] 

			drawList(arr, color(len(arr), low, high, left, j))
			time.sleep(speed)

		arr[left+1],arr[high] = arr[high],arr[left+1] 

		drawList(arr, color(len(arr), low, high, left, left + 1, swap = True))
		time.sleep(speed)

		return left+1
	  
	
	def quick_util(arr,low,high, speed): 
		if low < high: 
			pivot = util(arr,low,high)  
			quick_util(arr, low, pivot-1, speed) 
			quick_util(arr, pivot+1, high, speed)

		drawList(arr,['SeaGreen3' for _ in range(len(arr))])
		return arr



	def color(length, low, high, wall, idx, swap = False):
		colors = []
		for i in range(length):
			if i >= low and i <= high:
				colors.append('sky blue')
			else:
				colors.append('purple')

			if i == high:
				colors[i] = 'blue'
			elif i == wall:
				colors[i] = 'sky blue'
			elif i == idx:
				colors[i] = 'yellow2'
			if swap:
				if i == wall or i == idx:
					colors[i] = 'red'

		return colors


	low = 0
	high = len(arr)-1
	return quick_util(arr,low,high, speed)


#============================== Merge Sort ==============================
def merge_sort(arr,left,right, drawList=None, speed=None): 
    if left < right: 
        mid = (left+(right-1))//2
  
        merge_sort(arr, left, mid, drawList, speed) 
        merge_sort(arr, mid+1, right, drawList, speed) 
        merge(arr, left, mid, right, drawList, speed) 

    drawList(arr,['SeaGreen3' for _ in range(len(arr))])

    return arr

def merge(arr, left, mid, right, drawList=None, speed=None): 
    s1 = mid - left + 1
    s2 = right- mid
    # drawList(arr,['green' if x <= right else 'sky blue' for x in range(len(arr))])
    # time.sleep(speed)
    l_arr = [0] * (s1) 
    r_arr = [0] * (s2) 
 	
    for i in range(s1): 
        l_arr[i] = arr[left + i] 
  
    for j in range(s2): 
    	r_arr[j] = arr[mid + 1 + j] 
  
    l = r = 0          
    idx = left
    
    drawList(arr,['red' if x== idx else'green' if x >= left and x <= right else 'sky blue' for x in range(len(arr))])
    time.sleep(speed)
    
    while l < s1 and r < s2: 
        if l_arr[l] <= r_arr[r]:
        	arr[idx] = l_arr[l]
        	l += 1
        else: 
            arr[idx] = r_arr[r] 
            r += 1
        idx += 1

    drawList(arr,['red' if x== idx else'green' if x >= left and x <= right else 'sky blue' for x in range(len(arr))])
    time.sleep(speed)

  
    while l < s1: 
        arr[idx] = l_arr[l] 
        l += 1
        idx += 1
    drawList(arr,['red' if x== idx else'green' if x >= left and x<=right else 'sky blue' for x in range(len(arr))])
    time.sleep(speed)
  
    while r < s2: 
        arr[idx] = r_arr[r] 
        r += 1
        idx += 1
    drawList(arr,['red' if x== idx else'green' if x >= left and x<= right else 'sky blue' for x in range(len(arr))])
    time.sleep(speed)
 


	

#================================ Heap Sort ==============================
def heap(arr, drawList, speed):
	ret = []
	n = len(arr)
	temp = []

	for i in range(n-1):
		temp.append(arr.pop())
		h.heapify(temp)

		drawList(temp+arr,['red' if x == i else'sky blue' for x in range(n)])
		time.sleep(speed)
	
	for i in range(n-1):
		ret.append(h.heappop(temp))
		drawList(ret+temp,['green' if x < i else 'red' if x ==i else 'sky blue' for x in range(n)])
		time.sleep(speed)

	drawList(ret,['SeaGreen3' for _ in range(n)])


	return ret

#================================= Radix Sort ===========================

def radix(arr, drawList = None ,speed =None):
	num = len(str(max(arr)))

	for digit in range(num):
		bucket = [[] for i in range(10)]
		n = len(arr)
		drawList(arr,['sky blue' for x in range(n)])
		time.sleep(speed)
		for i in range(n):
			idx =  arr[i]// 10 ** digit % 10
			bucket[int(idx)].append(arr[i])
	
		arr = []
		for i in range(len(bucket)):
			temp = []
			arr.extend(bucket[i])
			temp.extend([x for x in bucket[i+1:]])
		drawList(arr+temp,['sky blue' for x in range(n)])
		time.sleep(speed)


	drawList(arr,['SeaGreen3' for _ in range(n)])
	return arr

#================================ Shell Sort ==========================
def shell(arr,drawList,speed):
    gap = len(arr)//2
    n = len(arr)
    while gap > 0:
    	drawList(arr,['blue' if x == gap else 'sky blue' for x in range(n)])
    	time.sleep(speed)
    	for i in range(gap, len(arr)):
    		val = arr[i]
    		idx = i
    		drawList(arr,['red' if x == idx-gap else'gold' if x == i else 'blue' if x == gap else 'green' if x <= idx  else 'sky blue' for x in range(n)])
    		time.sleep(speed)
    		while idx >= gap and val <arr[idx - gap]:
    			drawList(arr,['red' if x == idx-gap else'gold' if x == i else 'blue' if x == gap else 'green' if x <= idx else 'sky blue' for x in range(n)])
    			time.sleep(speed)
    			arr[idx] = arr[idx-gap]
    			idx = idx-gap
    		arr[idx] = val
    	gap //=2
    drawList(arr,['SeaGreen3' for _ in range(n)])
    return arr


 








	

if __name__ == '__main__':
	#arr = [random.randint(0,50_000) for x in range(10_000)]
	arr1 = arr = random.sample(range(1,21), 20)
	#example= [12,9,8,7,6,11,5,4,3,2,10,1]

	print(arr1)
	print(len(arr1))
	print(radix(arr1))


