def main():
    total=0
    f1=open('Result Card.txt','w')
    x=str(input('Enter Name:  '))
    f1.write(x + '\n')
    x=str(input('Father Name:  '))
    f1.write(x +'\n')
    f1.write('\n')
    f1.write('Subject' + '\t\t' + 'Total Marks' + '\t' + 'Obtained Marks' +'\n'+'\n')
    x=int(input('Physics:  '))
    total=total+x
    f1.write ('Physics'+'\t\t'+'100'+'\t\t'+str(x)+'\n'+'\n')
    x=int(input('Chemistry:  '))
    total=total+x
    f1.write ('Chemistry'+'\t'+'100'+'\t\t'+str(x)+'\n'+'\n')
    x=int(input('Biology:  '))    
    total=total+x
    f1.write ('Biology'+'\t\t'+'100'+'\t\t'+str(x)+'\n'+'\n')
    x=int(input('English:  '))    
    total=total+x
    f1.write ('English'+'\t\t'+'100'+'\t\t'+str(x)+'\n'+'\n')
    x=int(input('Urdu:  '))
    total=total+x
    f1.write ('Urdu'+'\t\t'+'100'+'\t\t'+str(x)+'\n'+'\n')
    f1.write ('\t\t'+'500'+'\t\t'+str(total))
    print ('Result Card Generated')
main()
    
    
