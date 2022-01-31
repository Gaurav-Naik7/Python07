i=0
sum=0
def pattern(no):
    global i
    global sum
    if(i<len(no)):
        sum=sum+int(no[i])
        i=i+1
        pattern(no)
    return sum

def main():
    x=input("Enter a number: ")
    ret=pattern(x)
    print("Summation of digits is: ",ret)

if __name__=="__main__":
    main()
