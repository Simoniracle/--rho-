from time import time 
import math 
import random 
def main():
    print('请输入 number 的值：') 
    number=int(input()) 
    print('number=',number) 
    time1=time() 
    pollard(number) 
    time2=time() 
    print('结束') 
    end=time2-time1 
    print(end) 
def f(x,number): 
    x=(x*x+1)%number 
    return x 
def pollard(num): 
    if(judge(num)): 
        print(num)
        return 
    a=2 
    b=a 
    a=f(a,num) 
    b=f(f(b,num),num) 
    while(b!=a): 
        p=math.gcd(abs(b-a),num) 
        if(p>1): 
            print (p) 
            num=num//p 
            print('num=',num) 
        a=f(a,num) 
        b=f(f(b,num),num) 
    return 0 
def judge(num): 
 if (num in [2,3,5,7,11,13]): 
     return True 
 if (num%2==0 or num%3==0 or num%5==0 or num%7==0 or num%11==0): 
     return False 
 a=random.randint(2,10) 
 t=num-1 
 k=0 
 while(t%2==0): 
     t=t//2 
     k=k+1
 x=pow(a,t,num) 
 while(k>0): 
     last=x 
     x=x*x%num 
     if(x==1 and last!=1 and last!=num-1): 
         return False 
     k=k-1 
 if(x!=1): 
     return False 
 return True
