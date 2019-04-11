def max_list_iter(int_list):  # must use iteration not recursion
   max = None
   try:
      for integer in int_list:
         if max == None or max < integer:
            max = integer
      return max
   except TypeError:
      raise ValueError
   
def reverse_rec(int_list):   # must use recursion
   temp = 0
   if int_list == []:
      return []
   if int_list == None:
      raise ValueError
   return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(val, low, high, lst):
   if lst == []:
      raise ValueError
   mid = (high//2) + low
   if high - low < 2 and lst[0] != val:
      return None
   if val < lst[mid]:
      return bin_search(val, low, mid, lst)
   elif val > lst[mid]:
      return bin_search(val, mid, high, lst)
   else:
      return mid
