def main():
    x=str(input('Enter First Character:  '))
    y=str(input('Enter Second Character:  '))
    a=ord(x)
    b=ord(y)
    c=a&b
    count=0
    if c&1==1:
        count=count+1
    if c&2==2:
        count=count+1
    if c&4==4:
        count=count+1
    if c&8==8:
        count=count+1
    if c&16==16:
        count=count+1
    if c&32==32:
        count=count+1
    if c&64==64:
        count=count+1
    if c&128==128:
        count=count+1
    if c&256==256:
        count=count+1
    print (f'In A and B,{count}(s) are same')

main()
main()
main()
    
