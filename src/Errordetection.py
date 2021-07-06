def VRC():
    print("INPUT YOUR CHOICE:")
    print("1.BINARY INPUT")
    print("2.STRING INPUT")
    choice=int(input("ENTER THE CHOICE :- "))
    if choice == 1:
        data = input("ENTER INPUT DATA (BINARY) - ")
        l=[]
        for j in range(len(data)//7):
            l.append(data[(7*j):(7*(j+1))])
        if not len(data)%7 == 0:
            l.append(data[-((len(data)%7)):len(data)])
        
    elif choice == 2:
        data = input("ENTER INPUT DATA (STRING) - ")
        data = [format(ord(x), 'b') for x in data]
        print("INPUT DATA IN BINARY FORM   - "+'  '.join(data)) 
        l=(list(data))


    for i in range(len(l)):
        flag=0
        for x in l[i]:
            if x=='1':
                flag+=1
        if flag % 2 == 0:
            l[i]=l[i]+'0'
        else:
            l[i]=l[i]+'1'
    print("TRANSMITTER SIDE :-")       
    print("TRANSMIT DATA WITH VRC    - "+' '.join(l)) 
    print("RECEIVER CHOICE:")
    print("1.SAME AS TRANSMITTED DATA")
    print("2.DIFFERENT INPUT")
    choice=int(input("ENTER THE CHOICE :- "))
    received_data=l[:]
    if choice ==2:
        received_data = list(input("ENTER THE DIFFERENT RECEIVER INPUT - "))
    l1=[]
    for j in range(len(received_data)//8):
        l1.append(received_data[(8*j):(8*(j+1))])
    if not len(received_data)%8 == 0:
            l1.append(received_data[-((len(received_data)%8)):len(received_data)])
    #print(l1)
    for i in range(len(l1)):
        flag=0
        for x in l1[i]:
            if x=='1':
               flag+=1
               #print(flag)
        if not(flag % 2 == 0):
            print("RECEIVER SIDE:-")
            print("DATA IS CORRUPTED - DATA IS DISCARDED - RESEND THE DATA")         
            return()
    print("RECEIVER SIDE:-")
    print("DATA MATCHED - DATA IS ACCEPTED!")
    return()


def CRC():
    divident=list(input("ENTER THE INPUT  - "))
    divisor=list(input("ENTER THE DIVISOR -"))
    len_div=len(divisor)-1	
    divident=divident + ['0'] * (len_div)
    divident=[int(x) for x in divident]
    divident_c=[int(x) for x in divident]
    divisor=[int(x) for x in divisor]
    for i in range(len(divident_c)-len_div):
        flag=0
        if divident_c[i]==0:
            continue
        else:
            for j in range(i,len(divisor)+i):
                if divident_c[j] == divisor[flag]:
                    divident_c[j]=0
                else:
                    divident_c[j]=1
                flag+=1
    trans_data=[]
    for i in range(len(divident_c)):
        trans_data.append(divident[i]+divident_c[i])
    trans_data1=[str(x) for x in trans_data]
    print("TRANSMITTER SIDE :-")       
    print("TRANSMIT DATA WITH CRC    :- " + ''.join(trans_data1)) 
    print("RECIVER CHOICE:")
    print("1.SAME AS TRANSMITTED DATA")
    print("2.DIFFERENT INPUT")
    choice=int(input("ENTER THE CHOICE - "))
    user_data=trans_data[:]
    if choice ==2:
        user_data = list(input("ENTER THE DIFFERENT RECEIVER INPUT - "))
    user_data=[int(x) for x in user_data]
    for i in range(len(user_data)-len_div):
        flag=0
        if user_data[i]==0:
            continue
        else:
            for j in range(i,len(divisor)+i):
                if user_data[j] == divisor[flag]:
                    user_data[j]=0
                else:
                    user_data[j]=1
                flag+=1
    for i in range(len(user_data)):
        if not (user_data[i] == 0):
            print("RECEIVER SIDE:-")
            print("DATA IS CORRUPTED - DATA IS DISCARDED - RESEND THE DATA")
            return()
    print("RECEIVER SIDE:-")
    print("DATA MATCHED - DATA IS ACCEPTED!")
    return()

def Checksum () :
    data_in = list(input("Enter the input \n"))
    data_in = [int(x) for x in data_in]
    int_arr = []
    for out_itr in range(len(data_in)//8):
        weight = 1
        count = 7
        inte = 0
        while count >=0 :
            inte+= (data_in[count+(out_itr*8)]  * weight )
            weight*=2
            count-=1
        int_arr.append(inte)
    bin_arr = []
    for i in int_arr :
        bin_arr.append(bin(i))
    sum =0
    for i in int_arr :
        sum += i
    checksum = bin(sum)[2:]
    checksum = [int(x) for x in checksum]
    for i in range(len(checksum)):
        if checksum[i] == 0:
            checksum[i] =1
        else :
            checksum[i] = 0
    print("Checksum is ")
    for i in checksum :
        print(i,end='')
    print()
    print("Data to be transmitter with checksum is ")
    count = 0
    for i in data_in :
        if count%8 == 0 and count != 0:
            print(' ',end='')
        print(i,end='')
        count+=1
    print(' ',end=' ')
    for i in checksum:
        print(i, end='')

    print("\n\nAt Receiver end ")
    print("Enter the choice \n1:For user data \n2:For transmitted data")
    choice = int(input())
    if choice == 1 :
        print("Enter the data ")
        user_data = list(input())
        user_data = [int(x) for x in user_data]
    else :
        print("No error occured ")
    if user_data == data_in+checksum :
        print("No error occured ")
    else:
        print("Error occured ")


def LRC():
    data_in = list(input("Enter the input \n"))
    LRC = []
    i = 0
    for out_itr in range(8):
        even_ones = 0
        for in_itr in range(len(data_in)//8):
            if data_in[out_itr+(in_itr*8)] == '1' :
                even_ones += 1
        if even_ones % 2 == 0 :
            LRC.append(0)
        else :
            LRC.append(1)
    data_transmitter = data_in + LRC
    data_transmitter = [int(x) for x in data_transmitter]
    print("LRC is ")
    for i in LRC :
        print(i,end = '')
    print()
    count = 0
    print("Data to be transmitted with LRC is ")
    for i in data_transmitter :
        if count % 8 == 0 and count != 0:
            print(' ',end='')
        print(i,end='')
        count+=1

    print("\n\nAt Receiver end ")
    print("Enter the choice \n1:No error \n2:Enter data with error")
    choice = int(input())
    if choice == 1 :
        print("Enter the data ")
        user_data = list(input())
        user_data = [int(x) for x in user_data]
    else :
        print("No error occured ")
    if user_data == data_transmitter :
        print("No error occured ")
    else:
        print("Error occured ")

def main():
    while (1):
        print("\n==========ERROR DETECTION CODES===============")
        print('''
        
              ``    `    `           `   `           `             `         ``                             
    +mhyd: yM-  /Mo oMhymm: /Mo oM/  -My   oMMs   oMhhNm: +Mo    `oddyydd                           
    NN/`  `MN:::dM. mN`.yM/ hM. mM:::yM:  sN-Nm   NN`.hM: dM`   `mN- ```                            
    `+dMo +MyooyMh :MdhMm. .Mh :MhoosMm  yM+:dM- /MdhMm. -My    oM+ :yNM:                           
  .+--oMy mN`  sM: hM. sM/ sM: hM.  +M+`dN+++yMo dM. yM/ yM:    :Md/-:Nm                            
  `+os+- `o/   +o  o+  .o/ +o  o+   /o`:o.   `o/ o/  .o: ++      .+oso+.       ''')
        
        print("===============================================")
        choice = int(input("Enter the choice \n1:For LRC\n2:For VRC\n3:For CRC\n4:For Checksum\n5:Exit\n"))
        if choice == 1 :
            LRC()
        elif choice == 2 :
            VRC()
        elif choice == 3:
            CRC()
        elif choice ==4:
            Checksum()
        elif choice == 5 :
            break
        else :
            print("Enter valid input")
            break
main()
print("================*****************=======================")