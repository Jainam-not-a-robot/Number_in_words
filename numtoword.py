def num2word(a): #This function will create convert numbers from 1 to 19 to their words
    if(a==0):
        num1=""
    if(a==1):
        num1="One"
    if(a==2):
        num1="Two"
    if(a==3):
        num1="Three"
    if(a==4):
        num1="Four"
    if(a==5):
        num1="Five"
    if(a==6):
        num1="Six"
    if(a==7):
        num1="Seven"
    if(a==8):
        num1="Eight"
    if(a==9):
        num1="Nine"
    if(a==10):
        num1="Ten"
    if(a==11):
        num1="Eleven"
    if(a==12):
        num1="Twelve"
    if(a==13):
        num1="Thirteen"
    if(a==14):
        num1="Fourteen"
    if(a==15):
        num1="Fifteen"
    if(a==16):
        num1="Sixteen"
    if(a==17):
        num1="Seventeen"
    if(a==18):
        num1="Eighteen"
    if(a==19):
        num1="Nineteen"
    
    return(num1)
def numcond(b,c):#This function takes unit's and ten's digit and returns by converting them into words(could have done this in num2word but did it here and am too lazy to change it)
    b=int(b)
    c=int(c)
    e=num2word(c)
    d=num2word(b)
    if(b==1):
        d=num2word(b*10+c)
        e=""
    if(b==2):
        d="Twenty"
    if(b==3):
        d="Thirty"
    if(b==4):
        d="Forty"
    if(b==5):
        d="Fifty"
    if(b==6):
        d="Sixty"
    if(b==7):
        d="Seventy"
    if(b==8):
        d="Eighty"
    if(b==9):
        d="Ninety"
    return(d,e)        
num=input("Enter the number:")
lnt=len(num)
num=int(num)
i=1
valnum=lnt/3#valnum will be helpful in making pairs of 3 numbers 
tridig=[0,0,0]#tridig is the group of 3 numbers
triword=["","",""]#triword is the group of 3 numbers in words(using numcond and num2word function)
while(lnt>0):
    if(lnt%3==1):#first we solve the first digit from left in case the length is 1,4,7... so that it is easy to make a pair of 3
        if(valnum<=1 and valnum>0):
            value=""
        if(valnum>1 and valnum<=2):
            value="Thousand"
        if(valnum>2 and valnum<=3):
            value="Million"
        dig=int(num/10**(lnt-1))
        num=num-dig*(10**(lnt-1))#removing the digits from num which will be printed ahead
        lnt-=1
        valnum=lnt/3
        triword=[num2word(dig)]
        print(f"{triword[0]} {value} ",end="")
        triword=["","",""]
        tridig=[0,0,0]
    if(lnt%3==2):
        if(valnum<=1 and valnum>0):
            value=""
        if(valnum>1 and valnum<=2):
            value="Thousand"
        if(valnum>2 and valnum<=3):
            value="Million"
        dig=int(num/10**(lnt-2))
        num=num-dig*(10**(lnt-2))
        lnt-=2
        valnum=lnt/3
        tridig=[int(dig/10),dig%10]
        triword[0],triword[1]=numcond(tridig[0],tridig[1])
        print(f"{triword[0]} {triword[1]} {value} ",end="")
        tridig=[0,0,0]
        triword=["","",""]
    if(num==0):
        break
    dig=int(num/(10**(lnt-3)))
    num=num-dig*(10**(lnt-3))
    i=0
    for i in range(0,3):
        sindig=int(dig%10)
        dig=dig/10
        tridig[i]=sindig
    i=0    
    for i in range(0,3):
        triword[i]=num2word(tridig[2-i])
    triword[1],triword[2]=numcond(tridig[1],tridig[0])
    if(valnum==1):
        value=""
    if(valnum==2):
        value="Thousand"
    if(valnum==3):
        value="Million"
    lnt=lnt-3
    valnum=lnt/3
    if(tridig[0]!=0):
        print(f"{triword[0]} hundred {triword[1]} {triword[2]} {value} ",end="")
    else:
        print(f"{triword[1]} {triword[2]} {value} ",end="")
