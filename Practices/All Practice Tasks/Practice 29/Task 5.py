def main():
    name=input('Name: ')
    first=''
    second=''

    for i in range (len(name)):
        if i==0:
            j=0
            while name[j]!=' ':
                first=first+name[j]
                j=j+1
        elif name [i] == ' ':
            j=i+1
            while j!=len(name):
                second=second+name[j]
                j+=1
    print('First Name: ',first)
    print('Last Name: ',second)

main()