def main():
   mar = 0.38
   jup = 2.34
   weight = float(input("What do you weigh on earth? "))
   print(("On Mars you would weigh " + "%.2f" + " pounds.\nOn Jupiter you would weigh " + "%.2f" + " pounds.") % (weight*mar, weight*jup))
if __name__ == "__main__":
   main()
