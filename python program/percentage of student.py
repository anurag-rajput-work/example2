s1 =  int(input( " enter the number of 1st subject : " ))
s2 =  int(input( " enter the number of 2nd subject : " ))
s3 =  int(input( " enter the number of 3rd subject : " ))
s4 =  int(input( " enter the number of 4th subject : " ))
s5 =  int(input( " enter the number of 5th subject : " ))
total = ( s1 + s2 + s3 + s4 +s5 )/5
print ( total )
if(  total >= 60 ):
    print (  " you are passed with 1st divison " )
elif(total < 59 and total > 50 ):
     print (  " you are passed with 2nd  divison " )
elif ( total < 49 and total > 40   ):
     print (  " you are passed with 3rd divison " )
else :
     print (  " you are fail" )
