a = 2
b = 90
c = 45

if a < c:
  if b < c:
    if a < b:
      print(a, b, c)
    else:
      print(b, a, c)
  else:
    if a < b:
      print(a, c, b)
    else:
      print(c, a, b)
else:
  if b < c:
    if a < b:
      print(b, c, a)
    else:
      print(c, b, a)
  else:
    if a < b:
      print(b, a, c) 
    else:
      print(c, a, b) 


if a < c:
  if b < c:
    if a < b:
      print(a, b, c)
    else:
      print(b, a, c)
  else:
    print(a, c, b)
else:
  if b < c:
    print(b, c, a)
  else:
    print(c, b, a)