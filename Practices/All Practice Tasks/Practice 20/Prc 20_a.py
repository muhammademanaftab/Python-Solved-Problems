def rectangular_box(r,c):
    for i in range (1,r-1):
        if i==1:
            for j in range (r*2):
                print ('*',end='')
            print()
        print ('*',end='')
        for k in range (2,r*2):
            print (' ',end='')
        print ('*')
        if i==r-2:
            for m in range (r*2):
                print ('*',end='')
r=int(input('Rows:  '))
c=int(input('Columns:  '))

rectangular_box(r,c)
