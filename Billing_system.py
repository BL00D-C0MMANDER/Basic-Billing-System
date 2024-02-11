#FORMAT ['PRODUCT_NAME','rate(per kg/per packet / per piece)']
#list index is product code
prod=[["Product Name", "Price per unit","Quantity"]]
def add():
    while True:
        name=input('Enter the name of the product:')
        q=int(input("Enter the quantity:"))
        nam=name.upper()+"* "+str(q)
        rate=float(input('Enter the rate (per unit):'))
        if [nam.upper(),rate] in prod:
            q2=prod.index([nam,rate])
            prod[q2][0]=nam[0:-1]+str(int(nam[-1])+1)
            prod[q2][2]+=q
            k=input('Do you wish to add another item[yes(y)/no(n)]:')
            if k=='n' or k=='N':
                break
        else:
            prod.append([nam,rate,q])
            print('Product code:',prod.index([nam,rate,q]))
            k=input('Do you wish to add another item[yes(y)/no(n)]:')
            if k=='n' or k=='N':
                break

def stock():
    for i in range(0,len(prod)):
        print(prod[i][0],'-',prod[i][1])

def shesh():
    op=int(input('enter product code:'))
    if int(prod[op][0][-1])>1:
        prod[op][0]=prod[op][0][0:-1]+str(int(prod[op][0][-1])-1)
    else:
        prod.pop(op)
def bill():
    net=0
    temp=[]
    z=True
    while z==True:
        c=int(input('product code:'))
        if c<len(prod):
            q=int(prod[c][0][-1])
            am=(prod[c][1])*prod[c][2]
            temp.append([c,am])
            net+=am
        else:
            print('invalid product code')
        k=input('wanna add another item[yes(y)/no(n)]:')
        if k=='n' or k=='N':
            z=False

    print("+--------------------------------------------------------------------------+")
    print(' |','PRODUCT NAME'+'  '*8,'  | ','AMOUNT(in Rs.)','  |')
   # print(' |                                                                            |')
    for i in range(len(temp)):
        print("+--------------------------------------------------------------------------+")
        print(' |',prod[temp[i][0]][0]+' '*(21-(len(prod[temp[i][0]][0]))+(prod[temp[i][0]][0]).count(' ')),str(temp[i][1])+'  '*(11-len(str(temp[i][1]))//2))
    print("+--------------------------------------------------------------------------+")
    print(' |                                                                             ')
    print(' |','TOTAL AMOUNT'+'   '*7,str(net)+'  '*(11-len(str(net))//2)), net
    print("+--------------------------------------------------------------------------+")


# ACTUAL PRINTING PART

print(''' What do you want to do:
                            1]ADD AN ITEM TO STOCK 
                            2]REMOVE AN ITEM (out of stock)
                            3]PREPARE A BILL ''')
while True:
    op=int(input('\nEnter the option:'))
    if op==1:
        add()
        stock()
    elif op==2:
        shesh()
        stock()
    elif op==3: 
        bill()
        print('\n\n Take the bill to exit store')
        
    else:
        print('\nINVALID OPTION')
    k=input('want to continue??[y/n]:')
    if k=='n' or k=='N':
        break
print('HAVE A NICE DAY!!')
        
        
    
    
    
    
     
