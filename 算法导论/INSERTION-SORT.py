#encoding=utf8
'''
算法导论，P10，插入排序
'''

def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j-1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key
	return A

if __name__ == '__main__':
	A = [5,2,4,6,1,3]
	print insertion_sort(A)
