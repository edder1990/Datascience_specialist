def sellect_sort(arr):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
        print(arr)
    return arr

def main():
	array = [1,2,3,34,5,3,4,3]
	sellect_sort(array)

if __name__ == "__main__":
	main()
