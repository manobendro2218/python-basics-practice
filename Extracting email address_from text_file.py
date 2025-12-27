
#Extracting email addresses and  counting the total number of addresses

#-----variables------
count=0

#------Opening file safely-------

fname=input('Enter file name here: ')

try:
    fh=open(fname)
except:
    print('Invalid file name', fname, 'could not be opened')
    quit()

#-------Extracting email----------

for lines in fh:
    if lines.startswith('From '):
        count+=1
        words=lines.split()
        email=words[1].upper()
        print(email)

print('Total email addresses on this file=',count)

