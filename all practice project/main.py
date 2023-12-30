'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def s(f,s):
    #f.sort()
    #s.sort()
    emp=[]
    aprox=[]
    aproxn=[]
    for i in f:
        
        for j in s:
            emp.append(i+j)

    #emp.sort()
    #print(emp)
    for k in emp:
        if k>100:
            aprox.append(k)
        if k<100:
            aproxn.append(k)


            
    p=min(aprox)
    p1=max(aproxn)
    
    maxe=max(emp)
    mini=min(emp)
    print(maxe,mini,p,p1,emp)
    
l1=[-1,3,8,2,9,5,79,98]
l2=[4,1,2,10,5,20,65,70]
s(l1,l2)
