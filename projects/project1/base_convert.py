baseABC = "0123456789ABCDEFG"
def convert(num, b):
   num = int(num)
   b = int(b)
   if num >= b:
      return convert(num//b, b) + convert(num % b, b)
   return baseABC[num]

def main():
   in_1 = input("Enter a number: ")
   in_2 = input("Enter a base you'd like to convert it to (2-16): ")
   print(convert(in_1, in_2))

if __name__ == "__main__":
   main()

