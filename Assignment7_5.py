def fact(no):
    if(no==0):
        return 1
    return no*fact(no-1)

def main():
    x=int(input("Enter a number: "))
    ret=fact(x)
    print("Factorial is : ",ret)

if __name__=="__main__":
    main()
