#Finding temperature value and making average in the equipment log

#User end
log=input('Enter the instrument log here:' )

try:
    lh=open(log)

except:
    print(log, 'could not be opened.')
    quit()

total=0
count=0

for line in lh:    #Finding temperature
    if not line.startswith('TEMP:'):
        continue
    #print(line)

    temp=float(line.split(':')[1].strip()) #data cleaning

    total+=temp
    count+=1

#Data acquisition:

if count>0:
    print('Total number of readings:',count)
    print('Total of the readings:', total)
    print('Average temperature:', total/count)

else:
    print('No temperature data found')


