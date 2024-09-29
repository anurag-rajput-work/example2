num =  int( input ("enter a number : " ) )
if ( num%3==0 ):
    print( " number is divisible by 3 " )
elif ( num%5==0 ):
    print( " number is divisible by 5 " )
elif( num%3==0 and num%5==0 ):
    print( " number is divisible by 3 or 5 " )
else :
    print( " number is not  divisible by 3 or 5 " )
