import matplotlib.pyplot as plt

def unipolar(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    return inp1
    

def polar_nrz_l(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    inp1=[-1 if i==0 else 1 for i in inp1]
    return inp1

def polar_nrz_i(inp):
    inp2=list(inp)
    lock=False
    for i in range(len(inp2)):
        if inp2[i]==1 and not lock:
            lock=True
            continue
        if lock and inp2[i]==1:
            if inp2[i-1]==0:
                inp2[i]=1
                continue
            else :
                inp2[i]=0
                continue
        if lock:
            inp2[i]=inp2[i-1]
    inp2=[-1 if i==0 else 1 for i in inp2]        
    return inp2
    

def polar_rz(inp):
    inp1=list(inp)
    inp1=[-1 if i==0 else 1 for i in inp1]
    li=[]
    for i in range(len(inp1)):
        li.append(inp1[i])
        li.append(0)
    return li
    

def Biphase_manchester(inp):
    inp1=list(inp)
    li,init=[],False
    for i in range(len(inp1)):
        if inp1[i]==0:
            li.append(-1)
            if not init:
                li.append(-1)
                init=True
            li.append(1)
        elif inp1[i]==1 :
            li.append(1)
            li.append(-1)
    return li        
    

def Differential_manchester(inp):
    inp1=list(inp)
    li,lock,pre=[],False,''
    for i in range(len(inp1)):
        if inp1[i]==0 and not lock:
            li.append(-1)
            li.append(-1)
            li.append(1)
            lock=True
            pre='S'
        elif inp1[i]==1 and not lock :
            li.append(1)
            li.append(1)
            li.append(-1)
            lock=True
            pre='Z'
        else:
            if inp1[i]==0:
                if pre=='S':
                    li.append(-1);li.append(1)
                else:
                    li.append(1);li.append(-1)
            else:
                if pre=='Z':
                    pre='S'
                    li.append(-1);li.append(1)
                else:
                    pre='Z'
                    li.append(1);li.append(-1)
                         
    return li                        


def AMI(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    lock=False
    for i in range(len(inp1)):
        if inp1[i]==1 and not lock:
            lock=True
            continue
        elif lock and inp1[i]==1:
            inp1[i]=-1
            lock=False
    return inp1  


def plotall(li):
    plt.subplot(7,1,1)
    plt.ylabel("Unipolar-NRZ")
    plt.title("Unipolar -NRZ")
    plt.plot(unipolar(li),color='red',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,2)
    plt.ylabel("P-NRZ-L")
    plt.title("NRZ-L")
    plt.plot(polar_nrz_l(li),color='blue',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,3)
    plt.ylabel("P-NRZ-I")
    plt.title("NRZ-I")
    plt.plot(polar_nrz_i(li),color='green',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,4)
    plt.ylabel("Polar-RZ")
    plt.title("Polar RZ")
    plt.plot(polar_rz(li),color='red',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,5)
    plt.ylabel("B_Man")
    plt.title("Manchester")
    plt.plot(Biphase_manchester(li),color='violet',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,6)
    plt.ylabel("Dif_Man")
    plt.title("Differential Manchester")
    plt.plot(Differential_manchester(li),color='red',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,7)
    plt.ylabel("A-M-I")
    plt.title("Alternate Mark Inversion")
    plt.plot(AMI(li),color='blue',drawstyle='steps-pre',marker='>')
    
    plt.show()

def plotunrz(li):
    plt.ylabel("Unipolar-NRZ")
    plt.plot(unipolar(li),color='red',drawstyle='steps-pre',marker='>')
    plt.title("Unipolar -NRZ")
    plt.show()

def plotpnrzl(li):
    plt.ylabel("P-NRZ-L")
    plt.plot(polar_nrz_l(li),color='blue',drawstyle='steps-pre',marker='>')
    plt.title("NRZ-L")
    plt.show()
def plotnrzi(li):
    plt.ylabel("P-NRZ-I")
    plt.plot(polar_nrz_i(li),color='green',drawstyle='steps-pre',marker='>')
    plt.title("NRZ-I")
    plt.show()
def plotprz(li):
    plt.ylabel("Polar-RZ")
    plt.plot(polar_rz(li),color='red',drawstyle='steps-pre',marker='>')
    plt.title("Polar RZ")
    plt.show()
def plotbman(li):
    plt.ylabel("B_Man")
    plt.plot(Biphase_manchester(li),color='violet',drawstyle='steps-pre',marker='>')
    plt.title("Manchester")
    plt.show()
def plotdifman(li):
    plt.ylabel("Dif_Man")
    plt.plot(Differential_manchester(li),color='red',drawstyle='steps-pre',marker='>')
    plt.title("Differential Manchester")
    plt.show()
def plotami(li):
    plt.ylabel("A-M-I")
    plt.plot(AMI(li),color='blue',drawstyle='steps-pre',marker='>')
    plt.title("Alternate Mark Inversion")
    plt.show()





    
        

if __name__=='__main__':
    print('''

    ================================================================================================
                                                                                                    
    -h/   .ho -hh:  /h. shhhh/    :hhhhy -hh-  /h` `+hddy` :shddy-  +hhhyo-  /h- +hy`  ss  .oyhdhs  
    yM-   oM/ yNmN` mm .Mh        dM`    hmmm` md /Nd-  :`hN/` .NM``Md  -mM. mN `MdMy -Mo sMs.  `:  
   `Md    NN `Ms:Mh-M+ sMdhh-    -Mmhh+ .Mo/Ms:M/`MN`    sM+   `NN +M+   dM.:Ms +M-yM:yM`+Mo :hhd-  
   oM+   /Mo oM- sMmM``Nm        yM-    sM. yMmN .MN`  . yM/  .hM/ mN` .yMo hM. md `mNNy +My   mN`  
   ydddh.sd. yy  `hdo -ddhhh`    ddhhh: hs  `hd+  /hmdho .sdddho. .ddhhho. `dy .d/  :dd-  +hdddh/   
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    `////-  //   :/`                                                                                
    oMo/hM+ oM/`yN/                                                                                 
    NMosNy` `mmmh.                                                                                  
   /Ms.-mM.  oMs                                                                                    
   hMyshmo   dM`                                                                                    
   `...`     ..                                                                                     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
      ``    `    `           `   `           `             `         ``                             
    +mhyd: yM-  /Mo oMhymm: /Mo oM/  -My   oMMs   oMhhNm: +Mo    `oddyydd                           
    NN/`  `MN:::dM. mN`.yM/ hM. mM:::yM:  sN-Nm   NN`.hM: dM`   `mN- ```                            
    `+dMo +MyooyMh :MdhMm. .Mh :MhoosMm  yM+:dM- /MdhMm. -My    oM+ :yNM:                           
  .+--oMy mN`  sM: hM. sM/ sM: hM.  +M+`dN+++yMo dM. yM/ yM:    :Md/-:Nm                            
  `+os+- `o/   +o  o+  .o/ +o  o+   /o`:o.   `o/ o/  .o: ++      .+oso+.      
  
  =================================================================================================
   ''')
    try:
        print("Enter the size of Encoded Data : ", end='\t')
        size=int(input())
    except:
        print("The size must be an integer value")
        exit()
    l =0
    flag=0
    li=[]
    print("\n =================================================================================================")
    selection=int(input("\n Enter your selection of encoding scheme. Press the following \n 1. Unipolar NRZ \n 2. Polar NRZ-l \n 3. Polar NRZ-I \n 4. Polar RZ \n 5. Manchester \n 6. Differential Manchester \n 7. Alternate Mark Inversion \n 8. All \n============================================================================================== \n Enter your selection : "))
    print("==================================================================================================")
    if(1<=selection<=8):
        print("Select Success")
        print('Enter the binary bits sequnece of length ',size,' bits : \n')
        for i in range(size):
            if((l==0) or (l==1)):
                try:
                    l=int(input())
                    li.append(l)
                except:
                    print("\n Data stream must have only binary values")
            else:
                print("\n Invalid Input")
                flag=1
                break
        if(flag==0):
            if(selection==1):
                plotunrz(li)
            elif(selection==2):
                plotpnrzl(li)
            elif(selection==3):
                plotnrzi(li)
            elif(selection==4):
                plotprz(li)
            elif(selection==5):
                plotbman(li)
            elif(selection==6):
                plotdifman(li)
            elif(selection==7):
                plotami(li)
            elif(selection==8):
                plotall(li)
            print("\n Encoding Success")
        else:
            print("\n Enter only binary inputs. Try Again!")
    else:
        print("\n Enter a valid selection")

    





    '''
    
    
    
    print('Enter the binary bits sequnece of length ',size,' bits : \n')
    for i in range(size):
        if(l==0) or (l==1):
            l=int(input())
            li.append(l)
        else:
            print("\n Invalid Input")
            flag=1
            break
if(flag==0):
    print("\n test")
else:
    print("\n Enter only binary inputs. Try Again!")
'''