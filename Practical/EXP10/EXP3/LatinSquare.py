def generateLatinSquare(n):
   first_half_end = n + 1

   for i in range(1, n + 1):
      first_half_start = first_half_end
      while (first_half_start <= n):
         print(first_half_start, end=" ")
         first_half_start += 1

      for second_half_start in range(1, first_half_end):
         print(second_half_start, end=" ")
      first_half_end -= 1
      print()
   print()

if __name__ == "__main__":
    n = int(input("enter the value of n"))
    generateLatinSquare(n)
#    generateLatinSquare(2)
#    generateLatinSquare(3)
#    generateLatinSquare(4)