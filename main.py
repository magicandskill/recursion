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
  
cache = {}

def _factorial(total, i):
  if(i == 0):
    return 1
  elif(i in cache):
    return cache[i]
  else:
    new_total = _factorial(total, i-1)
    cache[i] = new_total
    return new_total * i

def factorial(i):
  return _factorial(0, i)

total = re_add(0, 0, data)

print(total)
print(factorial(5))
print(factorial(15))
print(factorial(16))