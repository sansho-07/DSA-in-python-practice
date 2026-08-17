def printNnumber(n):
   if n==0:
      return 
   printNnumber(n-1)
   print(n)

x = printNnumber(6)
print(x)