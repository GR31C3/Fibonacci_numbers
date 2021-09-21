def fibo(k):
    if k <= 1:
        return k
    else:
        return(fibo(k-1) + fibo (k-2))
user_input = int (input('how many terms?'))
if user_input <= 0:
     print('not valid input')
else:
    print('fibonacci number: ')
    for i in range(user_input):
        print(fibo(i))
        
input('Press ENTER to exit')


