def sort_array(arr):
  odds = []
  for i in arr:
      if i % 2 !=0:
          odds.append(i)
  odds = sorted(odds, reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
