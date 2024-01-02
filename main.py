nums = [1, 2, 3, 4, 5, 6, 7]

def sum(data):
  total = 0
  for n in data:
    total += n
  return total

def re_add(current_sum, i, data):
  if(i >= len(data)):
    return current_sum
  else:
    new_sum = current_sum + data[i]
    return re_add(new_sum, i+1, data)

total = re_add(0, 0, nums)

print(total)
