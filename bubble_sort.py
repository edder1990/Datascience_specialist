def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
                print(arr)
    return arr

def main():
	array = [1,2,12,3,13,4,5,10]
	bubble_sort(array)

if __name__ == "__main__":
    main()
