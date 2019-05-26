yu=[1,0,0,0,0,0,0,0,0,0,0,0,0]
def shuchu():
    print('\t'*3+str(month)+'月',end='\n\n')
    print('Mon\tTues\tWed\tThur\tFri\tSat\tSun\t')
    for k in yu:
        s=sum(yu)
    print('\t'*(s%7),end='')
    yu[month]=day%7
    for i in range(1,day+1):
        print(i,end='\t')
        if (i+s)%7==0:
            print()
    print('\n\n')
for month in range(1,13):
    if month in [1,3,5,7,8,10,12]:
        day=31
        shuchu()
    if month in [4,6,9,11]:
        day=30
        shuchu()
    if month==2:
        day=28
        shuchu()
