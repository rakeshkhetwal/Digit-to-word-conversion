#program for conversion of digits to words
#Rakesh kumar khetwal


dic={0:' ',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
dic1={0:' ',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'ninteen'}
dic2={0:' ',1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

value=int(input("enter a no please"))
ones=value%10
tens=value//10
newtens=tens%10
hundred=value//100
newhundred=hundred%10
thousand=value//1000
exception=ones+newtens*10

if value<=9:
    print(dic[value])
elif value==10:
    print("ten")
elif 10<value<20:
    print(dic1[ones])
elif value<=99:
    print(dic2[tens]+ ' ' +dic[ones])
elif value==100:
    print("hundred")
elif value<=999:
    if 10<exception<20:
      print(dic[hundred]+' '+'hundred'+ ' '+dic1[ones])
    else:
      print(dic[hundred]+' '+'hundred'+ ' '+dic2[newtens]+' '+dic[ones])
elif value==1000:
    print("thousand")
elif value<=9999:
    if 10<exception<20:
        if newhundred==0:
             print(dic[thousand]+ ' '+'thousand'+' '+ dic[newhundred]+dic1[ones])
        else:   
             print(dic[thousand]+ ' '+'thousand'+' '+ dic[newhundred]+' '+'hundred'+' '+dic1[ones])
    else:
        if newhundred==0:
             print(dic[thousand]+ ' '+'thousand'+' '+ dic[newhundred]+dic2[newtens]+' '+dic[ones])
        else:
             print(dic[thousand]+ ' '+'thousand'+' '+ dic[newhundred]+' '+'hundred'+' '+dic2[newtens]+' '+dic[ones])

    

