
#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
hrs=input('Enter Hours:')
rate=input('Enter rate:')
try:
    h=float(hrs)
    r=float(rate)
except:
    print('Error: please insert numeric value!')
    quit()
def computepay(hours,rate):
    if h<=40:
        pay=h*r
    else:
        pay=(40*r)+(h-40)*(r*1.5)
    return pay
pay=computepay(h,r)
print('Pay:',pay)







