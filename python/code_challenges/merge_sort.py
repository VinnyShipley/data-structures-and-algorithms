'''
This algorithm splits lists in half recursively and sorts them once a base case is found
'''

def merge_sort(arr):
  n = len(arr)
  if n > 1:
    mid = n // 2
    left = arr[0: mid]
    right = arr[mid:]

    #sort left side
    merge_sort(left)

    #sort right side
    merge_sort(right)

    #merge sorted sides together
    merge(left, right, arr)
  return arr




def merge(left, right, arr):
  i = 0
  j = 0
  k = 0

  while i < len(left) and j < len(right):

    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1

    else:
      arr[k] = right[j]
      j += 1

    k += 1

  if i == len(left):
    arr[k:] = right[j:]

  else:
    arr[k:] = left[i:]



if __name__ == '__main__':
  old_list = [5,2,9,17,1,4, 14, 15,39,6]
  print(old_list)
  print(merge_sort(old_list))
