#Bin to Dec//Dec to Bin AND Dec to Hex//Hex to Dec
x=1
while x==1:
    choose= int(input(
        '''
Welcome to Python Multi Converter! Input a number from the following:

1- Decimal to Binary 
2- Binary to Decimal
3- Decimal to Hexadecimal
4- Hexadecimal to Decimal
5-Exit Converter
'''))
    if choose==1:
        y= int(input("Enter a binary number that you want to convert to binary: "))
        def dec2bin(number):
            z=bin(y)
            return z
        x= (dec2bin(y)[2:])
        print ("Binary conversion is: "+x )
    if choose==2:
        w=(input("Enter a decimal number that you want to convert to decimal: "))
        def dec2bin (number1):
            q= int(w,2)
            return q
        g= dec2bin(w)
        print("Decimal conversion is: "+ str(g) )

    if choose==3:
        a= int(input("Enter a decimal number that you want to convert to hexadecimal: "))
        def dec2hex (number2):
            b=hex(a)
            return b
        r= dec2hex(a)
        print("Hexadecimal conversion is: "+ str(r) )
    if choose==4:
        h=(input("Enter a hexadecimal number that you want to convert to decimal: "))
        def hex2dec (number3):
            i= int(h,16)
            return i
        v= hex2dec(h)
        print("Decimal conversion is: "+ str(v) )
    if choose==5:
        x+=1
        print ("Thank you and Goodbye!")
        exit()
        break



    
    
