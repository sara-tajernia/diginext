def minSwaps(arr):
	"""
	Given an array of n distinct elements, find the minimum number of swaps required to sort the array.
	:param arr: list
	:return: int
	"""
	arrpos = [*enumerate(arr)]
	arrpos.sort(key=lambda it: it[1])
	vis = {k: False for k in range(len(arr))}
	ans = 0
	for i in range(len(arr)):
		if vis[i] or arrpos[i][0] == i:
			continue

		cycle_size = 0
		j = i
		while not vis[j]:
			vis[j] = True
			j = arrpos[j][0]
			cycle_size += 1
		if cycle_size > 0:
			ans += (cycle_size - 1)

	return ans

if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    print('minimum number of swaps is ', minSwaps(arr))