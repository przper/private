def solution(n):
    lst=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    decimal=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    number=n
    result=''
    for ind,num in enumerate(lst):
        lst[ind]=int(number/decimal[ind])
        number-=lst[ind]*decimal[ind]
    for ind in range(len(lst)):
        result+=str((lst[ind]*roman[ind]))
    return result

solution(1666)
solution(4)
