def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
        print(arr)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right

def main():
	array =  [1,2,3,4,5,5,5,34,2,1,2,3]
	print(quick_sort(array))

if __name__ == "__main__":
	main()
