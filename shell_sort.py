import time
import pickle

def shell_sort(lst):
	print(" 0:",lst)
	print()
	length = len(lst)
	h = 1
	while h < length / 9:
		h = h * 3 + 1
	while h > 0:
		for i in range(h, length):
			j = i
			while j >= h and lst[j-h] > lst[j]:
				tmp = lst[j]
				lst[j] = lst[j-h]
				lst[j-h] = tmp
				j -= h
			print("{:02}: {}".format(i+1,lst))
		h = int(h / 3)

	return lst
#with open('sample_data.pkl','rb') as f:
#	lst =  pickle.load(f)

start = time.time()
lst = [20,6,2,3,4,5,6,6,10,12]
#lst = [20,6,2,3,4,5,6]
lst = shell_sort(lst)
print("elapsed {} sec".format(time.time() - start))
print(lst)
