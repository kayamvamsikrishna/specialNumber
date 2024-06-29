def isSpecial(a):
    dummy=a
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        f=1
        for i in range(1,rem+1):
            f*=i
        summ+=f
    if summ==a:
        return True
    else:
        return False
if __name__=='__main__':
    ll=int(input('Enter Lower limit'))
    up=int(input('Enter upper limit'))
    for a in range(ll,up+1):
        if isSpecial(a):
            print(a,' ',end='')