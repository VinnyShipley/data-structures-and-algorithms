

def insertion_sort(arr):

  for i in range(1, len(arr)):
    j = i - 1
    temp = arr[i]

    while j >= 0 and temp < arr[j]:
      arr[j + 1] = arr[j]
      j = j - 1
    arr[j + 1] = temp

  return arr




new_arr = [15,24,9,88,2,16]

print(insertion_sort(new_arr))
