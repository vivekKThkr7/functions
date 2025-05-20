def add(a, b):
  return a + b

sum = add(5, 3)

def get_min_max(numbers):
  return min(numbers), max(numbers)

min_val, max_val = get_min_max([1,2,3,5,7,5,3,6,9,22])
print(f"Min: {min_val}, Max: {max_val}")
