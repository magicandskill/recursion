data = [1, 2, 3, 4, 5, 6, 7]

def sum(data):
  total = 0
  for n in data:
    total += n
  return total

def re_add(sum, i, data):
  if(i >= len(data)):
    return sum
  else:
    return re_add(sum+data[i], i+1)

def _factorial(total, i):
  if(i == 0):
    return 1
  else:
    new_total = _factorial(total, i-1)
    return new_total * i

def factorial(i):
  return _factorial(0, i)

total = re_add(0, 0, data)

print(total)
print(factorial(5))
