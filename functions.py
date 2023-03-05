#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num_1,num_2,num_3):
    highest_number = max(num_1, num_2, num_3)
    print(highest_number)

max_num(num_1=50, num_2=2, num_3=1)

#Write a Python function called mult_list() to multiply all the numbers in a list.
List = [2, 5,2]
def mult_list(List):
    product =1
    for i in List:
        product = i * product
        print(product)

mult_list(List)

#Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    reversal = string[::-1]
    print(reversal)
rev_string(string='HelloHello')

#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(x,a,b):
    return x in range(a,b+1)

print(num_within(3,2,4))



#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)