#!/usr/bin/env python3

def happy_new_year():
    count_down=10
    
    while count_down>0:
            print(count_down)
            count_down-=1
            if (count_down==0):
                  print('Happy New Year!')
   

            
def square_integers(int_list):
      int_list_squared=[int_list_v**2 for int_list_v in int_list ]
      return (int_list_squared)


    

def fizzbuzz():
    for i in range(1,101):
            if i%3==0 and i%5==0:
                  print ('FizzBuzz')
            elif i%3==0:
                  print ('Fizz')
            elif i%5==0:
                  print ('Buzz')
            else: 
                 print (i)
            
      
