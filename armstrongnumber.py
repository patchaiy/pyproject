lower=int(input())
upper = int(input())
for num in range(lower, upper + 1):
   order = len(str(num))
   s= 0
   t= num
   while t > 0:
       digit = t % 10
       s+= digit ** order
       t//= 10
  if num == s:
       print(num)
