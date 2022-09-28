from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(size):
    min=i
    for j in range(i+1,size):
      if array[j] < array[min]:
        min=j
    (array[i],array[min]) = (array[min],array[i])
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
selectionSort(data, len(data))
print(data)
