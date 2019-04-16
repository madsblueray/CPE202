def bears(n):
   n = int(n)
   if n == 42:
      return True
   if n == 0 or n == 1:
      return False
   if n % 5 == 0:
      if bears(n - 42):
         return True
   if n % 3 == 0 or n % 4 == 0:
      strn = str(n)
      a = int(strn[len(strn)-1])
      if len(strn) <= 1:
         b = 1
      else:
         b = int(strn[len(strn)-2])
      if "0" in strn:
         pass      
      elif bears(n - (a * b)):
         return True
   if n % 2 == 0:
      if bears(n/2):
         return True
   return False

def main():
   in_ = input("How many bears would you like to use? ")
   print(bears(in_))

if __name__ == "__main__":
   main()


