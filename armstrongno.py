lower=int(input())
upper = int(input())
for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0
   t= num
   while t > 0:
       digit = t % 10
       sum += digit ** order
       t//= 10
  if num == sum:
       print(num)
